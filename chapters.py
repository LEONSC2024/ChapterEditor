import subprocess
import json
from PySide6.QtWidgets import QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QMessageBox, QInputDialog, QMenu
from PySide6.QtCore import Signal, Qt
import os

class ChapterManager(QWidget):
    chapter_selected = Signal(int)  # 信号用于章节点击跳转

    def __init__(self, video_path=None):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.chapter_list = QListWidget()
        self.layout.addWidget(self.chapter_list)

        self.chapters = []  # 存储 (title, time_ms)
        self.video_path = video_path
        self.previous_video_path = None

        self.chapter_list.itemClicked.connect(self.on_item_clicked)
        self.chapter_list.itemDoubleClicked.connect(self.on_item_double_clicked)
        self.chapter_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.chapter_list.customContextMenuRequested.connect(self.on_chapter_context_menu)

    def refresh_chapter_list(self):
        self.chapters.sort(key=lambda c: c[1])
        self.chapter_list.clear()
        for idx, (t, ms) in enumerate(self.chapters, start=1):
            display_text = f"{idx:02}. {t} - {self.format_time(ms)}"
            self.chapter_list.addItem(QListWidgetItem(display_text))
        # 保存 TXT 和 XML
        if self.video_path:
            self.export_mp4box_chapters_to_file(self.video_path)
            self.export_chapters_to_xml()

    def add_chapter(self, title, time_ms):
        """添加章节并立即更新章节 TXT 和 XML"""
        self.chapters.append((title, time_ms))
        self.refresh_chapter_list()

    def delete_chapter(self):
        row = self.chapter_list.currentRow()
        if row >= 0:
            self.chapters.pop(row)
            self.refresh_chapter_list()
        else:
            QMessageBox.warning(self, "提示", "请先选择要删除的章节。")

    def edit_chapter(self, index, new_title, new_time_ms):
        """编辑指定索引的章节，更新标题和时间，并实时生成 XML 文件"""
        if 0 <= index < len(self.chapters):
            self.chapters[index] = (new_title, new_time_ms)
            self.refresh_chapter_list()

    def on_item_clicked(self, item):
        """点击章节跳转"""
        index = self.chapter_list.row(item)
        _, time_ms = self.chapters[index]
        self.chapter_selected.emit(time_ms)

    def format_time(self, ms):
        s = int(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return f"{h:02}:{m:02}:{s:02}"

    def export_mp4box_chapters(self):
        """生成 MP4Box 可识别的章节文本"""
        # 按时间升序排序章节
        self.chapters.sort(key=lambda c: c[1])
        lines = []
        for idx, (title, time_ms) in enumerate(self.chapters, start=1):
            hours = int(time_ms / 3600000)
            minutes = int((time_ms % 3600000) / 60000)
            seconds = int((time_ms % 60000) / 1000)
            milliseconds = int(time_ms % 1000)
            time_str = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"
            lines.append(f"CHAPTER{idx:02}={time_str}")
            lines.append(f"CHAPTER{idx:02}NAME={title}")
        return "\n".join(lines)

    def export_mp4box_chapters_to_file(self, video_path=None):
        """将章节导出为 MP4Box 可识别的章节文件，保存为与视频同名的 TXT 文件"""
        if video_path is None:
            video_path = self.video_path
        if not video_path:
            return None

        chapters_text = self.export_mp4box_chapters()
        base_dir = os.path.dirname(video_path)
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        output_path = os.path.join(base_dir, f"{base_name}_chapters.txt")

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(chapters_text)

        return output_path

    def export_chapters_to_xml(self):
        """
        根据 self.chapters 列表生成 Matroska XML 格式章节文件，并保存。
        文件保存路径为视频同目录，文件名为 {视频名}_chapters.xml。
        """
        if not self.video_path:
            QMessageBox.warning(self, "错误", "未设置视频路径，无法导出章节 XML。")
            return None

        # 按时间升序排序章节
        self.chapters.sort(key=lambda c: c[1])

        try:
            base_dir = os.path.dirname(self.video_path)
            base_name = os.path.splitext(os.path.basename(self.video_path))[0]
            xml_path = os.path.join(base_dir, f"{base_name}_chapters.xml")

            xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>',
                         '<Chapters>',
                         '  <EditionEntry>']

            for idx, (title, time_ms) in enumerate(self.chapters, start=1):
                hours = int(time_ms / 3600000)
                minutes = int((time_ms % 3600000) / 60000)
                seconds = int((time_ms % 60000) / 1000)
                milliseconds = int(time_ms % 1000)
                timecode_str = f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:03}"

                xml_lines.append('    <ChapterAtom>')
                xml_lines.append(f'      <ChapterTimeStart>{timecode_str}</ChapterTimeStart>')
                xml_lines.append('      <ChapterDisplay>')
                xml_lines.append(f'        <ChapterString>{title}</ChapterString>')
                xml_lines.append('        <ChapterLanguage>eng</ChapterLanguage>')
                xml_lines.append('      </ChapterDisplay>')
                xml_lines.append('    </ChapterAtom>')

            xml_lines.append('  </EditionEntry>')
            xml_lines.append('</Chapters>')

            with open(xml_path, "w", encoding="utf-8") as f:
                f.write("\n".join(xml_lines))

            QMessageBox.information(self, "成功", f"章节 XML 文件已生成：\n{xml_path}")
            return xml_path

        except Exception as e:
            QMessageBox.warning(self, "错误", f"生成 MKV XML 章节文件失败：\n{e}")
            return None

    def clear_previous_txt(self):
        """删除上一个视频的 _chapters.txt 文件"""
        if self.video_path:
            base_name = os.path.splitext(os.path.basename(self.video_path))[0]
            base_dir = os.path.dirname(self.video_path)
            txt_path = os.path.join(base_dir, f"{base_name}_chapters.txt")
            if os.path.isfile(txt_path):
                try:
                    os.remove(txt_path)
                except Exception:
                    pass

    def load_mkv_chapters(self, video_path):
        """
        使用 ffprobe 提取 MKV 文件内置章节，并填入 self.chapters，更新界面，返回导出的章节文件路径。
        """
        if self.previous_video_path:
            old_base = os.path.splitext(os.path.basename(self.previous_video_path))[0]
            old_dir = os.path.dirname(self.previous_video_path)
            old_txt = os.path.join(old_dir, f"{old_base}_chapters.txt")
            if os.path.isfile(old_txt):
                try:
                    os.remove(old_txt)
                except Exception:
                    pass
        self.previous_video_path = video_path

        self.clear_previous_txt()
        # 清空现有章节和界面
        self.chapters.clear()
        self.chapter_list.clear()
        # 调用 ffprobe 提取章节
        try:
            cmd = [
                "ffprobe",
                "-v", "error",
                "-print_format", "json",
                "-show_chapters",
                "-i", video_path
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            info = json.loads(result.stdout)
            chapters = info.get("chapters", [])
            for chapter in chapters:
                start_time = chapter.get("start_time", 0)
                title = ""
                tags = chapter.get("tags", {})
                if isinstance(tags, dict):
                    title = tags.get("title", "")
                # ffprobe 的 start_time 是秒(float)，需转为毫秒
                try:
                    time_ms = int(float(start_time) * 1000)
                except Exception:
                    time_ms = 0
                # 标题为空则用"Chapter N"
                if not title:
                    idx = len(self.chapters) + 1
                    title = f"Chapter {idx}"
                self.chapters.append((title, time_ms))
            # 排序并刷新列表
            self.refresh_chapter_list()
            self.video_path = video_path
            # 导出章节为TXT并返回路径
            return self.export_mp4box_chapters_to_file(video_path)
        except Exception as e:
            QMessageBox.warning(self, "提取章节失败", f"无法提取 MKV 章节信息。\n{e}")
            return None

    def write_chapters_to_mkv(self):
        """调用 mkvmerge 写入章节到 MKV 文件"""
        if not self.video_path or not os.path.isfile(self.video_path):
            QMessageBox.warning(self, "错误", "视频文件不存在或路径未设置。")
            return

        base_dir = os.path.dirname(self.video_path)
        base_name = os.path.splitext(os.path.basename(self.video_path))[0]
        chapters_txt = os.path.join(base_dir, f"{base_name}_chapters.txt")
        if not os.path.isfile(chapters_txt):
            QMessageBox.warning(self, "错误", f"章节 TXT 文件不存在：{chapters_txt}")
            return

        # 先将 TXT 转为 XML
        chapters_xml = self.export_txt_to_mkv_xml(chapters_txt)
        if not chapters_xml or not os.path.isfile(chapters_xml):
            QMessageBox.warning(self, "错误", "章节 XML 文件生成失败。")
            return

        output_mkv = os.path.join(base_dir, f"{base_name}_with_chapters.mkv")

        cmd = [
            "mkvmerge",
            "-o", output_mkv,
            "--chapters", chapters_xml,
            self.video_path
        ]

        try:
            subprocess.run(cmd, check=True)
            QMessageBox.information(self, "成功", f"章节已写入新 MKV 文件：\n{output_mkv}")

            # 删除临时章节 TXT 文件，保持现有逻辑一致
            if os.path.isfile(chapters_txt):
                try:
                    os.remove(chapters_txt)
                except Exception:
                    pass

        except Exception as e:
            QMessageBox.warning(self, "错误", f"写入章节失败：\n{e}")
    def rename_chapter(self, index, new_title):
        """只修改章节名称，不改变时间"""
        if 0 <= index < len(self.chapters):
            time_ms = self.chapters[index][1]
            self.chapters[index] = (new_title, time_ms)
            self.refresh_chapter_list()

    def on_item_double_clicked(self, item):
        """双击章节名称以编辑"""
        index = self.chapter_list.row(item)
        if 0 <= index < len(self.chapters):
            old_title = self.chapters[index][0]
            new_title, ok = QInputDialog.getText(self, "修改章节名称", "新名称:", text=old_title)
            if ok and new_title:
                self.rename_chapter(index, new_title)

    def on_chapter_context_menu(self, pos):
        item = self.chapter_list.itemAt(pos)
        if item is None:
            return
        index = self.chapter_list.row(item)
        menu = QMenu()
        rename_action = menu.addAction("重命名章节")
        action = menu.exec_(self.chapter_list.mapToGlobal(pos))
        if action == rename_action:
            old_title = self.chapters[index][0]
            new_title, ok = QInputDialog.getText(self, "修改章节名称", "新名称:", text=old_title)
            if ok and new_title:
                self.rename_chapter(index, new_title)