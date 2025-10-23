# Technology Stack

## Core Framework
- **Python 3.10+** - Main programming language
- **PySide6** - Qt-based GUI framework for cross-platform desktop applications
- **Qt Multimedia** - Video playback and media handling

## External Dependencies
- **ffmpeg** - Video chapter extraction and MP4 processing
- **mkvmerge** (from mkvtoolnix) - MKV chapter writing and processing
- **MP4Box** (from GPAC) - MP4 chapter writing

## Project Structure
- `main1.0.py` - Application entry point
- `main_window.py` - Main GUI window with video player and chapter management
- `video_player.py` - Video playback widget using Qt Multimedia
- `chapters.py` - Chapter data management and file I/O
- `mp4_writer.py` - Video chapter writing utilities
- `调试/` - Debug and testing utilities

## Installation Requirements
```bash
pip install PySide6
brew install ffmpeg mkvtoolnix  # macOS
```

## Common Commands
- **Run application**: `python main1.0.py`
- **Package for macOS**: Use `调试/打包.py` with PyInstaller
- **Test chapter writing**: Use scripts in `调试/` folder

## File Formats
- **Input**: MP4, MKV video files
- **Chapter formats**: MP4Box TXT format, Matroska XML format
- **Temporary files**: `{video_name}_chapters.txt`, `{video_name}_chapters.xml`

## Architecture Notes
- Uses Qt's signal-slot pattern for UI communication
- Subprocess calls to external tools for video processing
- Automatic cleanup of temporary chapter files
- Theme system with dark/light mode support