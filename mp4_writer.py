import subprocess
import os
import re

def txt_to_matroska_xml(txt_path):
    """
    读取章节TXT文件，转换为Matroska章节XML格式字符串。
    TXT格式示例：
    CHAPTER01=00:00:00.000
    CHAPTER01NAME=Opening
    """
    with open(txt_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    chapters = {}
    time_pattern = re.compile(r'CHAPTER(\d{2})=(\d{2}:\d{2}:\d{2}\.\d{3})')
    name_pattern = re.compile(r'CHAPTER(\d{2})NAME=(.*)')

    for line in lines:
        line = line.strip()
        m_time = time_pattern.match(line)
        if m_time:
            idx = m_time.group(1)
            timecode = m_time.group(2)
            chapters.setdefault(idx, {})['time'] = timecode
            continue
        m_name = name_pattern.match(line)
        if m_name:
            idx = m_name.group(1)
            name = m_name.group(2)
            chapters.setdefault(idx, {})['title'] = name

    # 构建XML字符串
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<Chapters>',
           '  <EditionEntry>']
    for idx in sorted(chapters.keys()):
        chapter = chapters[idx]
        time_start = chapter.get('time', '00:00:00.000')
        title = chapter.get('title', '')
        xml.append('    <ChapterAtom>')
        xml.append(f'      <ChapterTimeStart>{time_start}</ChapterTimeStart>')
        xml.append('      <ChapterDisplay>')
        xml.append(f'        <ChapterString>{title}</ChapterString>')
        xml.append('        <ChapterLanguage>und</ChapterLanguage>')
        xml.append('      </ChapterDisplay>')
        xml.append('    </ChapterAtom>')
    xml.append('  </EditionEntry>')
    xml.append('</Chapters>')

    return "\n".join(xml)


def write_chapters(video_path):
    """
    根据视频类型（mp4/mkv）将同目录下的 {视频名}_chapters.txt 写入视频文件。
    - mp4: 写入 txt 并调用 MP4Box 写入章节
    - mkv: txt 转 xml，再用 mkvmerge 写入章节
    写入后临时文件替换原文件，并清理临时文件。
    """
    if not os.path.exists(video_path):
        raise FileNotFoundError(f"视频文件不存在: {video_path}")

    base_name = os.path.splitext(os.path.basename(video_path))[0]
    dir_name = os.path.dirname(video_path)
    txt_path = os.path.join(dir_name, f"{base_name}_chapters.txt")
    if not os.path.exists(txt_path):
        raise FileNotFoundError(f"章节TXT文件不存在: {txt_path}")

    ext = os.path.splitext(video_path)[1].lower()
    if ext == ".mp4":
        # MP4: 直接用 txt，调用 MP4Box 写入章节
        temp_output_path = os.path.join(dir_name, f"{base_name}_temp.mp4")
        # MP4Box 命令
        cmd = ["MP4Box", "-chap", txt_path, "-out", temp_output_path, video_path]
        print("执行命令:", " ".join(cmd))
        try:
            subprocess.run(cmd, check=True)
            os.replace(temp_output_path, video_path)
            print(f"章节已写入并覆盖原视频: {video_path}")
        except subprocess.CalledProcessError as e:
            print(f"写入章节失败: {e}")
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)
            raise
        # 无需清理 txt
    elif ext == ".mkv":
        # MKV: txt 转 xml，然后调用 mkvmerge
        xml_content = txt_to_matroska_xml(txt_path)
        xml_path = os.path.join(dir_name, f"{base_name}_chapters.xml")
        with open(xml_path, "w", encoding="utf-8") as f:
            f.write(xml_content)
        temp_output_path = os.path.join(dir_name, f"{base_name}_temp.mkv")
        cmd = ["mkvmerge", "-o", temp_output_path, "--chapters", xml_path, video_path]
        print("执行命令:", " ".join(cmd))
        try:
            subprocess.run(cmd, check=True)
            os.replace(temp_output_path, video_path)
            print(f"章节已写入并覆盖原视频: {video_path}")
        except subprocess.CalledProcessError as e:
            print(f"写入章节失败: {e}")
            if os.path.exists(temp_output_path):
                os.remove(temp_output_path)
            raise
        finally:
            if os.path.exists(xml_path):
                os.remove(xml_path)
    else:
        raise ValueError(f"暂不支持的文件类型: {ext}")

    return video_path

# 命令行测试入口
if __name__ == "__main__":
    video_path = input("请输入视频文件路径：").strip()
    write_chapters(video_path)