import subprocess
import json
import xml.etree.ElementTree as ET

def extract_mkv_chapters(video_path, output_txt=None, output_xml=None):
    """
    提取 MKV 自带章节，返回列表：
    [{"title": "Chapter 1", "start_time": "00:00:00.000", "end_time": "00:10:14.447"}, ...]
    """
    cmd = [
        "ffprobe",
        "-v", "error",
        "-print_format", "json",
        "-show_chapters",
        "-i", video_path
    ]

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        info = json.loads(result.stdout)
        chapters = info.get("chapters", [])
        chapter_list = []

        for idx, ch in enumerate(chapters, start=1):
            start_sec = float(ch.get("start_time", 0))
            end_sec = float(ch.get("end_time", 0))
            # 将秒数转为 HH:MM:SS.mmm
            h = int(start_sec // 3600)
            m = int((start_sec % 3600) // 60)
            s = start_sec % 60
            start_time_str = f"{h:02d}:{m:02d}:{s:06.3f}"

            # 章节标题
            title = ch.get("tags", {}).get("title", f"Chapter {idx}")

            chapter_list.append({
                "title": title,
                "start_time": start_time_str,
                "start_sec": start_sec,
                "end_sec": end_sec
            })

        if output_txt:
            with open(output_txt, "w", encoding="utf-8") as f:
                f.write(f"章节 ({len(chapter_list)} 个):\n")
                for i, ch in enumerate(chapter_list, start=1):
                    f.write(f"  {i}. {ch['start_time']}: {ch['start_sec']:.2f}s - {ch['end_sec']:.2f}s\n")

        if output_xml:
            chapters_elem = ET.Element("Chapters")
            edition_entry = ET.SubElement(chapters_elem, "EditionEntry")
            for ch in chapter_list:
                chapter_atom = ET.SubElement(edition_entry, "ChapterAtom")
                chapter_time_start = ET.SubElement(chapter_atom, "ChapterTimeStart")
                chapter_time_start.text = ch["start_time"]
                chapter_display = ET.SubElement(chapter_atom, "ChapterDisplay")
                chapter_string = ET.SubElement(chapter_display, "ChapterString")
                chapter_string.text = ch["title"]

            tree = ET.ElementTree(chapters_elem)
            tree.write(output_xml, encoding="utf-8", xml_declaration=True)

        return chapter_list

    except subprocess.CalledProcessError as e:
        print("提取章节失败:", e)
        return []
    except json.JSONDecodeError as e:
        print("解析章节 JSON 失败:", e)
        return []

import os

if __name__ == "__main__":
    video_path = input("请输入 MKV 文件路径: ").strip()
    xml_path = input("请输入章节 XML 输出文件路径（可选，留空则自动生成）: ").strip()
    output_xml_path = None
    if xml_path:
        # 如果用户输入的是目录，则自动生成文件名
        if os.path.isdir(xml_path):
            base_name = os.path.splitext(os.path.basename(video_path))[0]
            output_xml_path = os.path.join(xml_path, f"{base_name}_chapters.xml")
        else:
            output_xml_path = xml_path
    else:
        # 自动生成：视频文件所在目录 + 视频文件名 + "_chapters.xml"
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        dir_name = os.path.dirname(video_path)
        output_xml_path = os.path.join(dir_name, f"{base_name}_chapters.xml")

    chapters = extract_mkv_chapters(video_path, output_xml=output_xml_path)
    print(f"提取到 {len(chapters)} 个章节:")
    for idx, ch in enumerate(chapters, start=1):
        print(f"  {idx}. {ch['title']}: {ch['start_time']} ({ch['start_sec']:.2f}s) - {ch['end_sec']:.2f}s")