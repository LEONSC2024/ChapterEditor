import os
import subprocess

def write_chapters_inplace(video_path, chapter_xml_file):
    """
    使用 mkvmerge 将 Matroska XML 章节文件写入 MKV 视频文件，输出新文件（原文件路径 + "_with_chapters.mkv"）
    :param video_path: 原视频路径
    :param chapter_xml_file: 章节 XML 文件路径（Matroska XML 格式）
    """
    if not os.path.isfile(video_path):
        raise FileNotFoundError(f"视频文件不存在: {video_path}")
    if not os.path.isfile(chapter_xml_file):
        raise FileNotFoundError(f"章节文件不存在: {chapter_xml_file}")

    output_path = os.path.splitext(video_path)[0] + "_with_chapters.mkv"

    cmd = [
        "mkvmerge",
        "-o", output_path,
        "--chapters", chapter_xml_file,
        video_path
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"章节已写入新视频文件: {output_path}")
    except subprocess.CalledProcessError as e:
        print("mkvmerge 执行失败:", e.stderr.decode('utf-8'))

if __name__ == "__main__":
    try:
        video_path = input("请输入视频文件路径（确保路径正确且文件存在）: ").strip()
        if not video_path:
            raise ValueError("视频文件路径不能为空。")
        chapter_xml_file = input("请输入章节 XML 文件路径（确保路径正确且文件存在）: ").strip()
        if not chapter_xml_file:
            raise ValueError("章节 XML 文件路径不能为空。")
        write_chapters_inplace(video_path, chapter_xml_file)
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except Exception as e:
        print("发生未知错误:", e)