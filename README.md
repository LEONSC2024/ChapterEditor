# 🎬 MP4/MKV 章节编辑器

![wechat_2025-10-23_204011_125](https://github.com/user-attachments/assets/602e8c30-cc10-4e7f-b7b7-6e6ab87a12f5)


一个现代化的跨平台桌面应用程序，用于编辑MP4和MKV视频文件的章节信息。

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![PySide6](https://img.shields.io/badge/PySide6-GUI-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)

## ✨ 主要功能

- 📂 **视频加载** - 支持MP4和MKV格式视频文件
- 🎥 **实时播放** - 内置视频播放器，支持播放控制和进度跳转
- 📝 **章节管理** - 添加、删除、重命名章节，支持精确时间定位
- ⚡ **倍速播放** - 支持1.0x到4.0x多种播放倍速，点击弹出菜单选择
- 🎨 **现代主题** - 深色/浅色主题切换，现代化UI设计
- 💾 **章节写入** - 将章节信息直接写入视频文件
- 📤 **格式导出** - 支持导出MP4Box TXT和Matroska XML格式
- ⌨️ **快捷键** - 丰富的键盘快捷键支持

## 🚀 快速开始

### 系统要求

- Python 3.10 或更高版本
- PySide6
- FFmpeg
- MP4Box (GPAC)
- mkvmerge (MKVToolNix)

### 安装依赖

#### Python 依赖
```bash
pip install PySide6
```

#### 外部工具 (macOS)
```bash
brew install ffmpeg mkvtoolnix gpac
```

#### 外部工具 (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ffmpeg mkvtoolnix gpac
```

#### 外部工具 (Windows)
- 下载并安装 [FFmpeg](https://ffmpeg.org/download.html)
- 下载并安装 [MKVToolNix](https://mkvtoolnix.download/)
- 下载并安装 [GPAC](https://gpac.wp.imt.fr/downloads/)

### 运行应用

```bash
python main.py
```

## 📖 使用指南

### 基本操作

1. **打开视频** - 点击"📂 打开视频"按钮或直接拖拽视频文件到窗口
2. **播放控制** - 使用播放/暂停按钮或空格键控制播放
3. **添加章节** - 在需要的时间点点击"➕ 添加章节"
4. **编辑章节** - 右键点击章节可重命名或删除
5. **保存章节** - 点击"💾 保存章节到视频"将章节写入视频文件

### 快捷键

| 快捷键 | 功能 |
|--------|------|
| `空格` | 播放/暂停 |
| `←` | 后退10秒 |
| `→` | 快进10秒 |
| `↑` | 音量+10 |
| `↓` | 音量-10 |
| `M` | 静音/取消静音 |

### 倍速控制

点击倍速显示区域（如"1.0x"）会弹出倍速选择菜单：
- 1.0x (正常速度)
- 1.25x
- 1.5x
- 2.0x
- 3.0x
- 4.0x

### 主题切换

点击主题按钮可在深色和浅色主题间切换：
- 🌙 深色主题
- ☀️ 浅色主题

## 🏗️ 项目结构

```
├── main.py              # 应用程序入口
├── main_window.py       # 主窗口和UI逻辑
├── video_player.py      # 视频播放器组件
├── chapter_manager.py   # 章节管理逻辑
├── mp4_writer.py        # 视频章节写入工具
├── README.md           # 项目说明文档
└── 调试/               # 调试和打包工具
    ├── 写入测试.py      # 章节写入测试
    ├── 打包.py          # PyInstaller打包脚本
    └── 验测视频内容.py   # 视频内容验证
```

## 🔧 技术架构

### 核心技术栈
- **Python 3.10+** - 主要编程语言
- **PySide6** - 基于Qt的跨平台GUI框架
- **Qt Multimedia** - 视频播放和媒体处理

### 外部依赖
- **FFmpeg** - 视频章节提取和MP4处理
- **mkvmerge** - MKV章节写入和处理
- **MP4Box** - MP4章节写入

### 设计模式
- 使用Qt的信号-槽机制进行UI通信
- 通过子进程调用外部工具进行视频处理
- 自动清理临时章节文件
- 支持主题系统的深色/浅色模式

## 📁 支持的文件格式

### 输入格式
- **MP4** - MPEG-4视频文件
- **MKV** - Matroska视频文件

### 章节格式
- **MP4Box TXT** - MP4Box章节文本格式
- **Matroska XML** - Matroska章节XML格式

### 临时文件
- `{视频名}_chapters.txt` - MP4Box格式章节文件
- `{视频名}_chapters.xml` - Matroska格式章节文件

## 🎯 功能特性

### 视频播放
- ✅ 支持MP4/MKV格式
- ✅ 实时播放控制
- ✅ 进度条拖拽跳转
- ✅ 音量控制
- ✅ 多倍速播放
- ✅ 键盘快捷键

### 章节管理
- ✅ 从视频文件读取现有章节
- ✅ 添加新章节到当前播放位置
- ✅ 删除选中的章节（支持多选）
- ✅ 重命名章节
- ✅ 章节列表显示和跳转
- ✅ 右键菜单操作

### 文件操作
- ✅ 拖拽打开视频文件
- ✅ 导出章节到TXT/XML格式
- ✅ 将章节写入视频文件
- ✅ 自动清理临时文件

### 用户界面
- ✅ 现代化深色/浅色主题
- ✅ 响应式布局设计
- ✅ 直观的操作界面
- ✅ 状态提示和错误处理

## 🚀 打包发布

使用调试文件夹中的打包脚本：

```bash
python 调试/打包.py
```

这将使用PyInstaller创建独立的可执行文件。

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

本项目采用MIT许可证 - 详见LICENSE文件。

## 🙏 致谢

- [PySide6](https://doc.qt.io/qtforpython/) - 优秀的Python GUI框架
- [FFmpeg](https://ffmpeg.org/) - 强大的多媒体处理工具
- [MKVToolNix](https://mkvtoolnix.download/) - MKV文件处理工具
- [GPAC](https://gpac.wp.imt.fr/) - MP4文件处理工具

---

如果这个项目对你有帮助，请给个⭐️支持一下！
