
# 🎬 自用 MKV / MP4 章节编辑器

<img src="https://github.com/user-attachments/assets/d040bee2-4c99-4c81-bf24-e27a2ed6fc93" alt="界面预览" width="800"/>

> 🎥 电影、电视剧章节编辑与修改工具  
> 因找不到合适软件，遂使用 GPT 自行编写，macOS 完美运行。

---

## 💡 项目简介

**MKV/MP4 章节编辑器** 是一款基于 **Python + PySide6** 的跨平台 GUI 工具，  
用于 **编辑、管理视频章节（MP4 / MKV）**，并可写入视频文件中。  

### ✨ 功能特性
- ✅ 查看并加载视频内置章节  
- ✏️ 添加、删除、编辑章节  
- 🕒 自动时间排序，章节编号与时间同步  
- 🧾 编辑时会生成 `MP4Box TXT` 或 `Matroska XML` 章节文件 需要可以保存 
- 💾 写入 MKV 文件时自动封装并删除章节文件  
- 🖱 支持多选与框选批量删除  
- 🎚 支持 macOS、Windows、Linux 系统  （GPT说的，自用Mac OS正常运行）

---

## ⚙️ 环境依赖

请确保系统已安装以下依赖：

| 名称 | 用途 |
|------|------|
| `Python 3.10+` | 基础运行环境 |
| `PySide6` | 图形界面库 |
| `ffmpeg` | 视频章节提取与封装 |
| `mkvmerge` | MKV 专用章节写入工具 |

安装依赖命令：

```bash
pip install PySide6
brew install ffmpeg mkvtoolnix   # macOS 示例


⸻

🚀 使用方法

python main.py

程序启动后可执行以下操作：
	1.	导入视频文件（MP4 或 MKV）；
	2.	编辑章节：增加 / 删除 / 修改章节名称（目前修改不了）；
	3.	导出章节文件 或 直接写入视频；
	4.	章节写入成功后自动删除临时文件。

⸻

🧩 文件说明

文件	功能
main.py	程序主入口
main_window.py	主界面逻辑
chapters.py	章节管理与导出逻辑
mp4_writer.py	写入 MP4/MKV 文件逻辑
_chapters.txt / _chapters.xml	临时章节文件（自动删除）


⸻

🤝 贡献指南

欢迎提交 issue 或 pull request：
	•	🐞 Bug 报告：请详细描述操作步骤和错误信息
	•	💡 功能建议：描述需求和使用场景
	•	💻 代码贡献：遵循 PEP8 风格并提供测试案例

⸻

⚖️ License

本项目采用 MIT License
详情请见 LICENSE 文件。

⸻

作者：LEONSC2024
项目地址：https://github.com/LEONSC2024/ChapterEditor
