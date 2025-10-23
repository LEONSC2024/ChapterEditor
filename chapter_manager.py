# -*- coding: utf-8 -*-
"""
优化的章节管理器
负责章节数据的管理、排序、文件I/O等操作
"""

import os
import json
import subprocess
from typing import List, Dict, Optional
from PySide6.QtCore import QObject, Signal, QTimer


class Chapter:
    """章节数据类"""
    def __init__(self, name: str, time_ms: int):
        self.name = name
        self.time_ms = time_ms
    
    def __repr__(self):
        return f"Chapter(name='{self.name}', time_ms={self.time_ms})"


class ChapterManager(QObject):
    """章节管理器"""
    chapters_changed = Signal()  # 章节发生变化时发出信号
    
    def __init__(self):
        super().__init__()
        self._chapters: List[Chapter] = []
        self._video_path: Optional[str] = None
        self._update_timer = QTimer()
        self._update_timer.setSingleShot(True)
        self._update_timer.timeout.connect(self._delayed_save)
        
    @property
    def chapters(self) -> List[Chapter]:
        """获取按时间排序的章节列表"""
        return sorted(self._chapters, key=lambda c: c.time_ms)
    
    @property
    def video_path(self) -> Optional[str]:
        return self._video_path
    
    def set_video_path(self, path: str):
        """设置视频路径"""
        if self._video_path != path:
            self.clear_previous_files()
            self._video_path = path
            # 静默清空当前章节列表，避免显示上一个视频的章节
            self._chapters.clear()
    
    def clear_previous_files(self):
        """清理上一个视频的临时文件"""
        if not self._video_path:
            return
        
        base_name = os.path.splitext(os.path.basename(self._video_path))[0]
        base_dir = os.path.dirname(self._video_path)
        txt_path = os.path.join(base_dir, f"{base_name}_chapters.txt")
        
        if os.path.exists(txt_path):
            try:
                os.remove(txt_path)
                print(f"已删除旧章节文件: {txt_path}")
            except Exception as e:
                print(f"删除旧章节文件失败: {e}")
    
    def add_chapter(self, name: str, time_ms: int) -> bool:
        """添加章节"""
        # 检查是否已存在相同时间的章节（容差1秒）
        for chapter in self._chapters:
            if abs(chapter.time_ms - time_ms) < 1000:
                return False
        
        # 如果名称为空，自动生成
        if not name.strip():
            name = self._generate_chapter_name(time_ms)
        
        self._chapters.append(Chapter(name.strip(), time_ms))
        # 添加章节后重新编号所有默认章节名称
        self._renumber_default_chapters()
        self._schedule_update()
        return True
    
    def remove_chapter(self, index: int) -> bool:
        """删除指定索引的章节（基于排序后的列表）"""
        sorted_chapters = self.chapters
        if 0 <= index < len(sorted_chapters):
            chapter_to_remove = sorted_chapters[index]
            self._chapters.remove(chapter_to_remove)
            # 删除章节后重新编号所有默认章节名称
            self._renumber_default_chapters()
            self._schedule_update()
            return True
        return False
    
    def remove_chapters(self, indices: List[int]) -> int:
        """批量删除章节，返回实际删除的数量"""
        sorted_chapters = self.chapters
        chapters_to_remove = []
        
        for index in sorted(indices, reverse=True):
            if 0 <= index < len(sorted_chapters):
                chapters_to_remove.append(sorted_chapters[index])
        
        for chapter in chapters_to_remove:
            self._chapters.remove(chapter)
        
        if chapters_to_remove:
            # 删除章节后重新编号所有默认章节名称
            self._renumber_default_chapters()
            self._schedule_update()
        
        return len(chapters_to_remove)
    
    def rename_chapter(self, index: int, new_name: str) -> bool:
        """重命名章节"""
        sorted_chapters = self.chapters
        if 0 <= index < len(sorted_chapters):
            chapter = sorted_chapters[index]
            # 在原列表中找到对应的章节并修改
            for original_chapter in self._chapters:
                if original_chapter is chapter:
                    original_chapter.name = new_name.strip()
                    self._schedule_update()
                    return True
        return False
    
    def clear_chapters(self):
        """清空所有章节"""
        if self._chapters:
            self._chapters.clear()
            self._schedule_update()
    
    def load_from_video(self, video_path: str) -> bool:
        """从视频文件加载章节"""
        try:
            cmd = ["ffprobe", "-v", "error", "-print_format", "json", "-show_chapters", video_path]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            data = json.loads(result.stdout)
            chapters = data.get("chapters", [])

            if not chapters:
                return False

            self.clear_chapters()
            temp_chapters = []
            
            for ch in chapters:
                start_time = float(ch.get("start_time", 0))
                ms = int(start_time * 1000)
                name = ch.get("tags", {}).get("title", "")
                temp_chapters.append(Chapter(name, ms))
            
            # 按时间排序
            temp_chapters.sort(key=lambda c: c.time_ms)
            
            self._chapters = temp_chapters
            # 重新编号所有默认章节名称
            self._renumber_default_chapters()
            self._schedule_update()
            return True
            
        except Exception as e:
            print(f"读取视频章节失败: {e}")
            return False
    
    def load_from_txt(self, txt_path: str) -> bool:
        """从TXT文件加载章节"""
        if not os.path.exists(txt_path):
            return False
        
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            
            temp = {}
            for line in lines:
                line = line.strip()
                if line.startswith("CHAPTER") and "=" in line and "NAME=" not in line:
                    key, value = line.split("=", 1)
                    num = key[7:9]
                    temp[num] = {"time_str": value, "name": None}
                elif line.startswith("CHAPTER") and "NAME=" in line:
                    key, value = line.split("=", 1)
                    num = key[7:9]
                    if num in temp:
                        temp[num]["name"] = value
            
            self.clear_chapters()
            keys_sorted = sorted(temp.keys())
            for k in keys_sorted:
                t = temp[k]
                ms = self._parse_chapter_time(t["time_str"])
                name = t["name"] if t["name"] is not None else "Chapter"
                self._chapters.append(Chapter(name, ms))
            
            # 重新编号所有默认章节名称
            self._renumber_default_chapters()
            self._schedule_update()
            return True
            
        except Exception as e:
            print(f"无法读取章节TXT: {e}")
            return False
    
    def save_to_txt(self) -> bool:
        """保存章节到TXT文件"""
        if not self._video_path or not self._chapters:
            return False
        
        base_name = os.path.splitext(os.path.basename(self._video_path))[0]
        txt_path = os.path.join(os.path.dirname(self._video_path), f"{base_name}_chapters.txt")
        
        try:
            sorted_chapters = self.chapters
            lines = []
            
            for idx, chapter in enumerate(sorted_chapters, start=1):
                time_str = self._format_chapter_time(chapter.time_ms)
                lines.append(f"CHAPTER{idx:02}={time_str}")
                lines.append(f"CHAPTER{idx:02}NAME={chapter.name}")
            
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write("\n".join(lines))
            
            return True
            
        except Exception as e:
            print(f"保存章节TXT失败: {e}")
            return False
    
    def get_display_list(self) -> List[str]:
        """获取用于显示的章节列表"""
        sorted_chapters = self.chapters
        display_list = []
        
        for idx, chapter in enumerate(sorted_chapters, start=1):
            time_str = self._format_chapter_time(chapter.time_ms)
            display_list.append(f"{idx:02}. {time_str} - {chapter.name}")
        
        return display_list
    
    def _generate_chapter_name(self, time_ms: int) -> str:
        """根据时间位置生成章节名称"""
        # 临时生成名称，实际编号会在_renumber_default_chapters中统一处理
        return "Chapter"
    
    def _renumber_default_chapters(self):
        """重新编号所有默认章节名称（按时间顺序）"""
        sorted_chapters = self.chapters
        chapter_index = 1
        
        for chapter in sorted_chapters:
            # 只重新编号默认格式的章节名称
            if (chapter.name == "Chapter" or 
                chapter.name.startswith("Chapter ") or 
                (chapter.name.startswith("Chapter") and chapter.name[7:].isdigit())):
                chapter.name = f"Chapter {chapter_index:02d}"
            chapter_index += 1
    
    def _parse_chapter_time(self, time_str: str) -> int:
        """解析章节时间字符串为毫秒"""
        try:
            if "." in time_str:
                hhmmss, ms = time_str.split(".")
                ms = int(ms)
            else:
                hhmmss = time_str
                ms = 0
            h, m, s = map(int, hhmmss.split(":"))
            total_ms = ((h * 60 + m) * 60 + s) * 1000 + ms
            return total_ms
        except Exception:
            return 0
    
    def _format_chapter_time(self, ms: int) -> str:
        """格式化毫秒为章节时间字符串"""
        h, rem = divmod(ms // 1000, 3600)
        m, s = divmod(rem, 60)
        ms_rem = ms % 1000
        return f"{h:02}:{m:02}:{s:02}.{ms_rem:03}"
    
    def _schedule_update(self):
        """安排延迟更新"""
        self._update_timer.start(100)  # 100ms延迟
    
    def _delayed_save(self):
        """延迟保存和发出信号"""
        self.save_to_txt()
        self.chapters_changed.emit()