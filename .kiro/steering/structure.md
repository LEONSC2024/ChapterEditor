# Project Structure

## Root Directory
```
├── main1.0.py              # Application entry point
├── main_window.py          # Main GUI window (1000+ lines)
├── video_player.py         # Video playback widget
├── chapters.py             # Chapter management logic
├── mp4_writer.py           # Video chapter writing utilities
├── README.md               # Project documentation (Chinese)
└── 调试/                   # Debug and testing folder
    ├── 写入测试.py          # Chapter writing tests
    ├── 打包.py              # PyInstaller packaging script
    ├── 章节结构             # Chapter structure reference
    └── 验测视频内容.py      # Video content validation
```

## Code Organization

### Main Application (`main1.0.py`)
- Simple entry point that initializes QApplication and MainWindow
- Sets application name and starts event loop

### Main Window (`main_window.py`)
- **UI Setup**: Video player, chapter list, controls, progress bar
- **Theme Management**: Dark/light theme switching with detailed CSS
- **Video Controls**: Play/pause, seek, speed control, keyboard shortcuts
- **Chapter Management**: Add/delete chapters, jump to timestamps
- **File I/O**: Load video files, export chapter files, write to video

### Video Player (`video_player.py`)
- Encapsulates Qt Multimedia components (QMediaPlayer, QVideoWidget)
- Provides playback controls and position tracking
- Handles keyboard shortcuts for video navigation

### Chapter Management (`chapters.py`)
- Chapter data structure and sorting
- Export to MP4Box TXT and Matroska XML formats
- Integration with ffprobe for chapter extraction
- Context menu for chapter editing

### Video Writing (`mp4_writer.py`)
- Format conversion between TXT and XML chapter formats
- Subprocess integration with MP4Box and mkvmerge
- Temporary file management and cleanup

## Naming Conventions
- **Files**: Snake_case for Python modules
- **Classes**: PascalCase (MainWindow, VideoPlayer, ChapterManager)
- **Methods**: Snake_case (load_video, add_chapter, export_chapters)
- **UI Elements**: Descriptive names with widget type suffix (_button, _list, _slider)

## File Management
- Temporary chapter files use pattern: `{video_name}_chapters.{txt|xml}`
- Automatic cleanup of temporary files on application close
- Output videos for MKV: `{video_name}_with_chapters.mkv`
- In-place replacement for MP4 files after chapter writing