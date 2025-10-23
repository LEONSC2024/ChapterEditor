# ===== 高级现代化主题样式 =====
""" 深色主题
QPushButton 样式的每个属性均添加详细注释，说明其用途
"""
#
# ===== 高级现代化主题样式（深色） =====
# 每个选择器前添加注释，属性后添加注释说明
#
DARK_THEME = """
/* 整体窗口 */
QWidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #23262b, stop:1 #181a1f); /* 背景渐变色 */
    color: #e0e0e0; /* 文字颜色 */
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; /* 字体 */
    font-size: 15px; /* 字体大小 */
}

/* 普通按钮 */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2d3136, stop:1 #23262b); /* 按钮背景渐变 */
    color: #e0e0e0; /* 按钮文字颜色 */
    border: none; /* 无边框 */
    border-radius: 16px; /* 按钮圆角 */
    padding: 8px 18px; /* 按钮内边距 */
    font-weight: 200; /* 按钮文字粗细 */
    box-shadow: 0 2px 8px rgba(0,0,0,0.13); /* 按钮阴影（Qt不支持，仅参考） */
    transition: all 0.15s; /* 按钮属性变化过渡（Qt不支持，仅参考） */
}

/* 鼠标悬停按钮 */
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #31363b, stop:1 #3a4047); /* 按钮悬停背景渐变 */
    color: #53aaff; /* 按钮悬停文字颜色 */
    box-shadow: 0 4px 18px rgba(60,120,220,0.13); /* 按钮悬停阴影（Qt不支持，仅参考） */
    transform: scale(1.035); /* 按钮悬停缩放（Qt不支持，仅参考） */
}

/* 按钮按下状态 */
QPushButton:pressed {
    background: #22262e; /* 按钮按下时背景色 */
    color: #3a99fc; /* 按钮按下时文字颜色 */
    transform: scale(0.98); /* 按钮按下缩放（Qt不支持，仅参考） */
}

/* 普通标签 */
QLabel {
    color: #e0e0e0; /* 标签文字颜色 */
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; /* 字体 */
    font-size: 15px; /* 字体大小 */
    font-weight: 500; /* 字体粗细 */
}

/* 章节列表控件 */
QListWidget {
    background: rgba(45,49,54,0.89); /* 列表背景色 */
    color: #e0e0e0; /* 列表文字颜色 */
    border-radius: 20px; /* 列表圆角 */
    border: 1.5px solid #34363b; /* 列表边框 */
    padding: 6px 6px 6px 6px; /* 列表内边距 */
    font-size: 15px; /* 列表字体大小 */
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; /* 字体 */
}

/* 列表项默认状态 */
QListWidget::item {
    background: rgba(38,41,47,0.95); /* 单项背景色 */
    border-radius: 14px; /* 单项圆角 */
    margin: 6px 4px; /* 单项外边距 */
    padding: 8px 14px; /* 单项内边距 */
    box-shadow: 0 2px 8px rgba(0,0,0,0.13); /* 单项阴影（Qt不支持，仅参考） */
    transition: all 0.15s; /* 单项属性过渡（Qt不支持，仅参考） */
}

/* 列表项鼠标悬停状态 */
QListWidget::item:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #2d3640, stop:1 #3a99fc); /* 单项悬停背景渐变 */
    color: #fff; /* 单项悬停文字颜色 */
    box-shadow: 0 4px 14px rgba(60,120,220,0.13); /* 单项悬停阴影（Qt不支持，仅参考） */
}

/* 列表项选中状态 */
QListWidget::item:selected {
    background: #3a99fc; /* 单项选中背景色 */
    color: #fff; /* 单项选中文字颜色 */
    border: none; /* 无边框 */
}

/* 下拉框 */
QComboBox {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #2d3136, stop:1 #23262b); /* 下拉框背景渐变 */
    color: #e0e0e0; /* 下拉框文字颜色 */
    border-radius: 12px; /* 下拉框圆角 */
    border: 1.5px solid #444; /* 下拉框边框 */
    padding-left: 10px; /* 下拉框左内边距 */
    min-height: 32px; /* 下拉框最小高度 */
    font-size: 15px; /* 下拉框字体大小 */
    transition: all 0.15s; /* 下拉框属性过渡（Qt不支持，仅参考） */
}

/* 下拉框悬停状态 */
QComboBox:hover {
    border: 1.5px solid #3a99fc; /* 下拉框悬停边框颜色 */
    background: #2d3640; /* 下拉框悬停背景色 */
    color: #53aaff; /* 下拉框悬停文字颜色 */
}

/* 下拉框下拉项区域 */
QComboBox QAbstractItemView {
    background: #2d3136; /* 下拉项背景色 */
    color: #e0e0e0; /* 下拉项文字颜色 */
    border-radius: 10px; /* 下拉项圆角 */
    selection-background-color: #3a99fc; /* 选中项背景色 */
    selection-color: #fff; /* 选中项文字颜色 */
    font-size: 15px; /* 下拉项字体大小 */
}

/* 横向滑槽 */
QSlider::groove:horizontal { 
    height: 8px; /* 滑槽高度 */
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3a99fc, stop:1 #31363b); /* 滑槽背景渐变 */
    border-radius: 4px; /* 滑槽圆角 */
}

/* 横向滑块 */
QSlider::handle:horizontal { 
    background: qradialgradient(cx:.5, cy:.5, radius:.8, fx:.5, fy:.5, stop:0 #3a99fc, stop:1 #23262b); /* 滑块背景渐变 */
    border: 2px solid #3a99fc; /* 滑块边框 */
    width: 18px; height: 18px; /* 滑块尺寸 */
    margin: -6px 0; /* 滑块外边距 */
    border-radius: 9px; /* 滑块圆角 */
    transition: all 0.15s; /* 滑块属性过渡（Qt不支持，仅参考） */
}

/* 横向滑块悬停 */
QSlider::handle:horizontal:hover {
    background: #2d3136; /* 滑块悬停背景色 */
    border: 2.5px solid #53aaff; /* 滑块悬停边框颜色 */
}

/* 已滑动部分 */
QSlider::sub-page:horizontal { 
    background: #3a99fc; /* 已滑动部分颜色 */
    border-radius: 4px; /* 圆角 */
}

/* 未滑动部分 */
QSlider::add-page:horizontal { 
    background: #444; /* 未滑动部分颜色 */
    border-radius: 4px; /* 圆角 */
}
"""
""" 浅色主题
QPushButton 样式的每个属性均添加详细注释，说明其用途
"""
#
# ===== 高级现代化主题样式（浅色） =====
# 每个选择器前添加注释，属性后添加注释说明
#
LIGHT_THEME = """
/* 整体窗口 */
QWidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #f7fafc, stop:1 #e9e9f3); /* 背景渐变色 */
    color: #23272f; /* 文字颜色 */
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; /* 字体 */
    font-size: 15px; /* 字体大小 */
}

/* 普通按钮 */
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #f5f7fa, stop:1 #e6eaf0); /* 按钮背景渐变 */
    border: none; /* 无边框 */
    border-radius: 16px; /* 按钮圆角 */
    padding: 8px 18px; /* 按钮内边距 */
    color: #23272f; /* 按钮文字颜色 */
    font-weight: 500; /* 按钮文字粗细 */
    box-shadow: 0 2px 8px rgba(180,180,200,0.08); /* 按钮阴影（Qt不支持，仅参考） */
    transition: all 0.15s; /* 按钮属性变化过渡（Qt不支持，仅参考） */
}

/* 鼠标悬停按钮 */
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #e3e9f1, stop:1 #c9d6e3); /* 按钮悬停背景渐变 */
    color: #1565c0; /* 按钮悬停文字颜色 */
    box-shadow: 0 4px 18px rgba(80,120,200,0.13); /* 按钮悬停阴影（Qt不支持，仅参考） */
    transform: scale(1.035); /* 按钮悬停缩放（Qt不支持，仅参考） */
}

/* 按钮按下状态 */
QPushButton:pressed {
    background: #d8e2ef; /* 按钮按下时背景色 */
    color: #174377; /* 按钮按下时文字颜色 */
    transform: scale(0.98); /* 按钮按下缩放（Qt不支持，仅参考） */
}

/* 普通标签 */
QLabel {
    color: #21242a; /* 标签文字颜色 */
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; /* 字体 */
    font-size: 15px; /* 字体大小 */
    font-weight: 500; /* 字体粗细 */
}

/* 章节列表控件 */
QListWidget {
    background: rgba(255,255,255,0.83); /* 列表背景色 */
    color: #222; /* 列表文字颜色 */
    border-radius: 20px; /* 列表圆角 */
    border: 0.5px solid #e4e8ec; /* 列表边框 */
    padding: 6px 6px 6px 6px; /* 列表内边距 */
    font-size: 15px; /* 列表字体大小 */
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif; /* 字体 */
}

/* 列表项默认状态 */
QListWidget::item {
    background: rgba(255,255,255,0.92); /* 单项背景色 */
    border-radius: 14px; /* 单项圆角 */
    margin: 6px 4px; /* 单项外边距 */
    padding: 8px 14px; /* 单项内边距 */
    box-shadow: 0 2px 8px rgba(180,180,200,0.06); /* 单项阴影（Qt不支持，仅参考） */
    transition: all 0.15s; /* 单项属性过渡（Qt不支持，仅参考） */
}

/* 列表项鼠标悬停状态 */
QListWidget::item:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #e6f0fa, stop:1 #dbeafe); /* 单项悬停背景渐变 */
    color: #1565c0; /* 单项悬停文字颜色 */
    box-shadow: 0 4px 14px rgba(80,120,200,0.13); /* 单项悬停阴影（Qt不支持，仅参考） */
}

/* 列表项选中状态 */
QListWidget::item:selected {
    background: #3a99fc; /* 单项选中背景色 */
    color: #fff; /* 单项选中文字颜色 */
    border: none; /* 无边框 */
}

/* 下拉框 */
QComboBox {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #f8fafc, stop:1 #e8eaf1); /* 下拉框背景渐变 */
    color: #23272f; /* 下拉框文字颜色 */
    border-radius: 12px; /* 下拉框圆角 */
    border: 1.5px solid #d3d3db; /* 下拉框边框 */
    padding-left: 10px; /* 下拉框左内边距 */
    min-height: 32px; /* 下拉框最小高度 */
    font-size: 15px; /* 下拉框字体大小 */
    transition: all 0.15s; /* 下拉框属性过渡（Qt不支持，仅参考） */
}

/* 下拉框悬停状态 */
QComboBox:hover {
    border: 1.5px solid #3a99fc; /* 下拉框悬停边框颜色 */
    background: #eaf4ff; /* 下拉框悬停背景色 */
    color: #174377; /* 下拉框悬停文字颜色 */
}

/* 下拉框下拉项区域 */
QComboBox QAbstractItemView {
    background: #fff; /* 下拉项背景色 */
    color: #23272f; /* 下拉项文字颜色 */
    border-radius: 10px; /* 下拉项圆角 */
    selection-background-color: #3a99fc; /* 选中项背景色 */
    selection-color: #fff; /* 选中项文字颜色 */
    font-size: 15px; /* 下拉项字体大小 */
}

/* 横向滑槽 */
QSlider::groove:horizontal { 
    height: 8px; /* 滑槽高度 */
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #c3e0fa, stop:1 #f5f7fa); /* 滑槽背景渐变 */
    border-radius: 4px; /* 滑槽圆角 */
}

/* 横向滑块 */
QSlider::handle:horizontal { 
    background: qradialgradient(cx:.5, cy:.5, radius:.8, fx:.5, fy:.5, stop:0 #3a99fc, stop:1 #dbeafe); /* 滑块背景渐变 */
    border: 2px solid #3a99fc; /* 滑块边框 */
    width: 18px; height: 18px; /* 滑块尺寸 */
    margin: -6px 0; /* 滑块外边距 */
    border-radius: 9px; /* 滑块圆角 */
    transition: all 0.15s; /* 滑块属性过渡（Qt不支持，仅参考） */
}

/* 横向滑块悬停 */
QSlider::handle:horizontal:hover {
    background: #fff; /* 滑块悬停背景色 */
    border: 2.5px solid #1565c0; /* 滑块悬停边框颜色 */
}

/* 已滑动部分 */
QSlider::sub-page:horizontal { 
    background: #3a99fc; /* 已滑动部分颜色 */
    border-radius: 4px; /* 圆角 */
}

/* 未滑动部分 */
QSlider::add-page:horizontal { 
    background: #ddd; /* 未滑动部分颜色 */
    border-radius: 4px; /* 圆角 */
}
"""
DARK_THEME = """
QWidget {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                               stop:0 #23262b, stop:1 #181a1f);
    color: #e0e0e0;
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
    font-size: 15px;
}
QPushButton {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #2d3136, stop:1 #23262b);
    color: #e0e0e0;
    border: none;
    border-radius: 16px;
    padding: 8px 18px;
    font-weight: 500;
    box-shadow: 0 2px 8px rgba(0,0,0,0.13); /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
    transition: all 0.15s; /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QPushButton:hover {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                stop:0 #31363b, stop:1 #3a4047);
    color: #53aaff;
    box-shadow: 0 4px 18px rgba(60,120,220,0.13); /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
    transform: scale(1.035); /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QPushButton:pressed {
    background: #22262e;
    color: #3a99fc;
    transform: scale(0.98); /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QLabel {
    color: #e0e0e0;
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
    font-size: 15px;
    font-weight: 500;
}
QListWidget {
    background: rgba(45,49,54,0.89);
    color: #e0e0e0;
    border-radius: 20px;
    border: 1.5px solid #34363b;
    padding: 6px 6px 6px 6px;
    font-size: 15px;
    font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
}
QListWidget::item {
    background: rgba(38,41,47,0.95);
    border-radius: 14px;
    margin: 6px 4px;
    padding: 8px 14px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.13); /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
    transition: all 0.15s; /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QListWidget::item:hover {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                                stop:0 #2d3640, stop:1 #3a99fc);
    color: #fff;
    box-shadow: 0 4px 14px rgba(60,120,220,0.13); /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QListWidget::item:selected {
    background: #3a99fc;
    color: #fff;
    border: none;
}
QComboBox {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                stop:0 #2d3136, stop:1 #23262b);
    color: #e0e0e0;
    border-radius: 12px;
    border: 1.5px solid #444;
    padding-left: 10px;
    min-height: 32px;
    font-size: 15px;
    transition: all 0.15s; /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QComboBox:hover {
    border: 1.5px solid #3a99fc;
    background: #2d3640;
    color: #53aaff;
}
QComboBox QAbstractItemView {
    background: #2d3136;
    color: #e0e0e0;
    border-radius: 10px;
    selection-background-color: #3a99fc;
    selection-color: #fff;
    font-size: 15px;
}
QSlider::groove:horizontal { 
    height: 8px;
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #3a99fc, stop:1 #31363b);
    border-radius: 4px;
}
QSlider::handle:horizontal { 
    background: qradialgradient(cx:.5, cy:.5, radius:.8, fx:.5, fy:.5, stop:0 #3a99fc, stop:1 #23262b);
    border: 2px solid #3a99fc;
    width: 18px; height: 18px;
    margin: -6px 0;
    border-radius: 9px;
    transition: all 0.15s; /* 标准CSS属性，但Qt Style Sheet不支持；不会生效，但不影响程序运行 */
}
QSlider::handle:horizontal:hover {
    background: #2d3136;
    border: 2.5px solid #53aaff;
}
QSlider::sub-page:horizontal { 
    background: #3a99fc;
    border-radius: 4px;
}
QSlider::add-page:horizontal { 
    background: #444;
    border-radius: 4px;
}
"""
import os
import subprocess
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFileDialog, QComboBox, QListWidget, QMessageBox, QSplitter, QSlider, QInputDialog, QMenu
)
from PySide6.QtCore import Qt, QTimer
from video_player import VideoPlayer
from mp4_writer import write_chapters
from chapter_manager import ChapterManager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎬 MP4章节封面编辑器")
        self.setGeometry(200, 100, 1200, 750)
        self.setAcceptDrops(True)

        self.video_path = None
        self.is_slider_dragging = False
        
        # 使用新的章节管理器
        self.chapter_manager = ChapterManager()
        self.chapter_manager.chapters_changed.connect(self.on_chapters_changed)

        self.setup_ui()
        self.set_theme("深灰")

    def setup_ui(self):
        splitter = QSplitter(Qt.Horizontal)
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)

        # 视频播放器
        self.video_player = VideoPlayer()
        self.video_player.setMinimumHeight(400)

        # 播放进度条
        progress_layout = QHBoxLayout()
        self.current_time_label = QLabel("00:00:00")
        self.total_time_label = QLabel("00:00:00")
        self.progress_slider = QSlider(Qt.Horizontal)
        self.progress_slider.setRange(0, 1000)
        self.progress_slider.sliderPressed.connect(self.on_slider_pressed)
        self.progress_slider.sliderReleased.connect(self.on_slider_released)
        self.progress_slider.sliderMoved.connect(self.on_slider_moved)
        progress_layout.addWidget(self.current_time_label)
        progress_layout.addWidget(self.progress_slider, stretch=1)
        progress_layout.addWidget(self.total_time_label)

        # 控制区
        control_layout = QHBoxLayout()
        self.open_button = QPushButton("📂 打开视频")
        self.open_button.clicked.connect(self.open_video)
        control_layout.addWidget(self.open_button)

        self.play_button = QPushButton("▶ 播放/暂停")
        self.play_button.clicked.connect(lambda: self.safe_play_pause())
        control_layout.addWidget(self.play_button)

        self.rewind_button = QPushButton("⏪ 倒退10秒")
        self.rewind_button.clicked.connect(lambda: self.video_player.seek_relative(-10))
        control_layout.addWidget(self.rewind_button)

        self.forward_button = QPushButton("⏩ 快进10秒")
        self.forward_button.clicked.connect(lambda: self.video_player.seek_relative(10))
        control_layout.addWidget(self.forward_button)

        # 倍速控制 - 点击弹出菜单
        self.speed_label = QLabel("倍速：")
        self.current_speed = "1.0x"
        self.speed_button = QPushButton(self.current_speed)
        self.speed_button.setStyleSheet("font-weight: bold; color: #3a99fc; min-width: 50px;")
        self.speed_button.clicked.connect(self.show_speed_menu)
        control_layout.addWidget(self.speed_label)
        control_layout.addWidget(self.speed_button)

        # 主题切换 - 改为点击按钮
        self.current_theme = "深灰"
        self.theme_button = QPushButton("🌙 深色")
        self.theme_button.clicked.connect(self.toggle_theme)
        control_layout.addWidget(self.theme_button)

        self.save_button = QPushButton("💾 保存章节到视频")
        self.save_button.clicked.connect(self.save_chapters_to_video)
        control_layout.addWidget(self.save_button)
        control_layout.addStretch()

        # 倍速选项列表（用于弹出菜单）
        self.speed_options = ["1.0x", "1.25x", "1.5x", "2.0x", "3.0x", "4.0x"]

        video_layout = QVBoxLayout()
        video_layout.addWidget(self.video_player)
        video_layout.addLayout(progress_layout)
        video_layout.addLayout(control_layout)
        video_widget = QWidget()
        video_widget.setLayout(video_layout)

        # 章节管理区
        chapter_widget = QWidget()
        chapter_layout = QVBoxLayout(chapter_widget)
        chapter_layout.setAlignment(Qt.AlignTop)
        title = QLabel("📘 章节管理")
        title.setStyleSheet("font-size:16px; font-weight:bold; margin-bottom:6px;")
        chapter_layout.addWidget(title)
        chapter_widget.setMinimumWidth(350)
        chapter_widget.setMaximumWidth(350)

        self.chapter_list = QListWidget()
        self.chapter_list.setSelectionMode(QListWidget.ExtendedSelection)  # 启用多选
        self.chapter_list.itemDoubleClicked.connect(self.jump_to_chapter)
        self.chapter_list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.chapter_list.customContextMenuRequested.connect(self.show_chapter_context_menu)
        chapter_layout.addWidget(self.chapter_list, stretch=1)

        btn_layout = QHBoxLayout()
        self.add_chapter_btn = QPushButton("➕ 添加章节")
        self.add_chapter_btn.clicked.connect(self.add_chapter)
        self.del_chapter_btn = QPushButton("🗑 删除章节")
        self.del_chapter_btn.clicked.connect(self.delete_chapter)
        btn_layout.addWidget(self.add_chapter_btn)
        btn_layout.addWidget(self.del_chapter_btn)
        chapter_layout.addLayout(btn_layout)

        # 状态栏
        self.status_label = QLabel("就绪")
        self.status_label.setAlignment(Qt.AlignLeft)
        self.status_label.setStyleSheet("""
            font-family: 'Segoe UI', 'PingFang SC', 'Microsoft YaHei', sans-serif;
            font-size: 15px;
            color: #3a99fc;
            padding: 6px 8px;
            background: rgba(58,153,252,0.07);
            border-radius: 10px;
        """)
        main_layout.addWidget(self.status_label)

        splitter.addWidget(video_widget)
        splitter.addWidget(chapter_widget)
        splitter.setSizes([850, 350])
        self.setCentralWidget(splitter)

        # 进度条样式已在主题中定义，无需重复设置

        # 定时器同步进度条 - 降低更新频率以提升性能
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(200)  # 从500ms改为200ms，提升响应性但不过于频繁

    # ===== 快捷键支持 =====
    def keyPressEvent(self, event):
        if not self.video_player or not hasattr(self.video_player, "player"):
            return super().keyPressEvent(event)

        key = event.key()
        if key == Qt.Key_Space:
            self.safe_play_pause()
            event.accept()
        elif key == Qt.Key_Right:
            self.video_player.seek_relative(10)
            self.safe_set_status("快进 10 秒")
            event.accept()
        elif key == Qt.Key_Left:
            self.video_player.seek_relative(-10)
            self.safe_set_status("后退 10 秒")
            event.accept()
        elif key == Qt.Key_Up:
            vol = min(self.video_player.player.volume() + 10, 100)
            self.video_player.player.setVolume(vol)
            self.safe_set_status(f"音量 {vol}%")
            event.accept()
        elif key == Qt.Key_Down:
            vol = max(self.video_player.player.volume() - 10, 0)
            self.video_player.player.setVolume(vol)
            self.safe_set_status(f"音量 {vol}%")
            event.accept()
        elif key == Qt.Key_M:
            current_vol = self.video_player.player.volume()
            if current_vol > 0:
                self.video_player.player.setVolume(0)
                self.safe_set_status("静音")
            else:
                self.video_player.player.setVolume(50)
                self.safe_set_status("取消静音，音量 50%")
            event.accept()
        else:
            super().keyPressEvent(event)

    # ===== 原有方法保持不变 =====
    def safe_play_pause(self):
        try:
            if self.video_player and hasattr(self.video_player, "toggle_play"):
                self.video_player.toggle_play()
                self.safe_set_status("播放/暂停切换")
        except Exception as e:
            self.safe_set_status(f"播放失败: {e}")

    def set_theme(self, theme_name):
        # 简化的主题设置
        if theme_name == "深灰":
            self.setStyleSheet(DARK_THEME)
        else:
            self.setStyleSheet(LIGHT_THEME)
        
        # 更新倍速按钮主题样式
        self.update_speed_button_theme()

    def closeEvent(self, event):
        # 清理临时文件
        if self.chapter_manager:
            self.chapter_manager.clear_previous_files()
        super().closeEvent(event)

    def safe_set_status(self, text):
        # 避免在窗口关闭后操作已删除对象
        if hasattr(self, "status_label") and self.status_label and not sip_is_deleted(self.status_label):
            QTimer.singleShot(0, lambda: self.status_label.setText(text))

    def show_speed_menu(self):
        """显示倍速选择菜单"""
        menu = QMenu(self)
        
        for speed in self.speed_options:
            action = menu.addAction(speed)
            action.setCheckable(True)
            action.setChecked(speed == self.current_speed)
            action.triggered.connect(lambda checked, s=speed: self.set_speed(s))
        
        # 在按钮下方显示菜单
        button_pos = self.speed_button.mapToGlobal(self.speed_button.rect().bottomLeft())
        menu.exec(button_pos)

    def set_speed(self, speed_text):
        """设置播放倍速"""
        try:
            # 更新显示
            self.current_speed = speed_text
            self.speed_button.setText(speed_text)
            
            # 设置播放器倍速
            speed = float(speed_text.replace('x', ''))
            self.video_player.player.setPlaybackRate(speed)
            self.safe_set_status(f"倍速已设置为 {speed}x")
        except Exception as e:
            self.safe_set_status(f"设置倍速失败: {e}")

    def toggle_theme(self):
        """切换主题"""
        if self.current_theme == "深灰":
            self.current_theme = "浅白"
            self.theme_button.setText("☀️ 浅色")
            self.set_theme("浅白")
        else:
            self.current_theme = "深灰"
            self.theme_button.setText("🌙 深色")
            self.set_theme("深灰")
        
        # 更新倍速按钮样式以适应新主题
        self.update_speed_button_theme()

    def update_speed_button_theme(self):
        """更新倍速按钮的主题样式"""
        if self.current_theme == "深灰":
            self.speed_button.setStyleSheet("font-weight: bold; color: #3a99fc; min-width: 50px;")
        else:
            self.speed_button.setStyleSheet("font-weight: bold; color: #3a99fc; min-width: 50px;")

    def change_speed(self, text):
        """保持兼容性的旧方法"""
        self.set_speed(text)

    # ===== 打开视频 =====
    def open_video(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "", "视频文件 (*.mp4 *.mkv)"
        )
        if file_path:
            self.load_video_file(file_path)

    def check_path_permission(self, file_path):
        # 检查文件是否存在且可读
        if not os.path.isfile(file_path):
            QMessageBox.warning(self, "提示", "文件不存在！")
            return False
        if not os.access(file_path, os.R_OK):
            QMessageBox.warning(self, "提示", "文件不可读，请检查权限！")
            return False
        if not (file_path.lower().endswith(".mp4") or file_path.lower().endswith(".mkv")):
            QMessageBox.warning(self, "提示", "只支持 mp4 或 mkv 视频文件！")
            return False
        return True

    def load_video_file(self, file_path):
        if not self.check_path_permission(file_path):
            return

        # 设置新的视频路径到章节管理器
        self.chapter_manager.set_video_path(file_path)
        self.video_path = file_path
        self.video_player.load_video(file_path)

        # 设置窗口标题
        video_title = os.path.basename(file_path)
        try:
            cmd = ["ffprobe", "-v", "error", "-show_entries", "format_tags=title",
                   "-of", "default=noprint_wrappers=1:nokey=1", file_path]
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.stdout.strip():
                video_title = result.stdout.strip()
        except Exception:
            pass
        self.setWindowTitle(f"🎬 {video_title}")
        self.safe_set_status(f"已加载：{os.path.basename(file_path)}")
        self.video_player.player.durationChanged.connect(self.update_total_time)
        
        # 尝试从视频或TXT文件加载章节
        if not self.chapter_manager.load_from_video(file_path):
            base_name = os.path.splitext(os.path.basename(file_path))[0]
            txt_path = os.path.join(os.path.dirname(file_path), f"{base_name}_chapters.txt")
            if not self.chapter_manager.load_from_txt(txt_path):
                # 如果视频没有章节且没有对应的TXT文件，确保显示空列表
                self.update_chapter_display()

    # ===== 从视频读取章节 =====


    def export_chapters_to_xml(self):
        """
        导出当前章节为标准 Matroska XML 章节文件，保存到视频同目录下，命名为 {视频名}_chapters.xml
        """
        if not self.video_path or not self.chapters:
            return
        base_name = os.path.splitext(os.path.basename(self.video_path))[0]
        xml_path = os.path.join(os.path.dirname(self.video_path), f"{base_name}_chapters.xml")
        try:
            import xml.etree.ElementTree as ET
            # Root element
            chapters_elem = ET.Element("Chapters")
            edition_entry = ET.SubElement(chapters_elem, "EditionEntry")
            for idx, c in enumerate(self.chapters, start=1):
                chapter_atom = ET.SubElement(edition_entry, "ChapterAtom")
                ms_total = c["time_ms"]
                h, rem = divmod(ms_total // 1000, 3600)
                m, s = divmod(rem, 60)
                ms_rem = ms_total % 1000
                # Matroska uses HH:MM:SS.nnnnnnnnn (9 digits for nanoseconds)
                time_str = f"{h:02}:{m:02}:{s:02}.{ms_rem:03}000000"
                chapter_time_start = ET.SubElement(chapter_atom, "ChapterTimeStart")
                chapter_time_start.text = time_str
                chapter_display = ET.SubElement(chapter_atom, "ChapterDisplay")
                chapter_string = ET.SubElement(chapter_display, "ChapterString")
                chapter_string.text = c["name"]
                chapter_language = ET.SubElement(chapter_display, "ChapterLanguage")
                chapter_language.text = "und"
            # Write XML with declaration and pretty print
            tree = ET.ElementTree(chapters_elem)
            # Pretty print using minidom
            try:
                import xml.dom.minidom
                rough_string = ET.tostring(chapters_elem, encoding="utf-8")
                reparsed = xml.dom.minidom.parseString(rough_string)
                pretty_xml = reparsed.toprettyxml(indent="  ", encoding="utf-8")
                with open(xml_path, "wb") as f:
                    f.write(pretty_xml)
            except Exception:
                # fallback: write as is
                tree.write(xml_path, encoding="utf-8", xml_declaration=True)
            self.safe_set_status(f"Matroska章节XML已生成: {os.path.basename(xml_path)}")
        except Exception as e:
            self.safe_set_status(f"生成XML章节文件失败: {e}")



    def update_chapter_display(self):
        """更新章节显示列表"""
        self.chapter_list.clear()
        display_list = self.chapter_manager.get_display_list()
        for item_text in display_list:
            self.chapter_list.addItem(item_text)

    def add_chapter(self):
        if not self.video_path:
            self.safe_set_status("请先加载视频！")
            return
        
        current_time = self.video_player.player.position()
        
        # 使用章节管理器添加章节
        if self.chapter_manager.add_chapter("", current_time):
            self.safe_set_status("已添加章节")
        else:
            QMessageBox.warning(self, "提示", "该时间点附近已存在章节！")

    def delete_chapter(self):
        selected_rows = [self.chapter_list.row(item) for item in self.chapter_list.selectedItems()]
        if not selected_rows:
            QMessageBox.warning(self, "提示", "请先选择要删除的章节。")
            return
        
        # 确认删除
        if len(selected_rows) > 1:
            reply = QMessageBox.question(
                self, "确认删除", 
                f"确定要删除选中的 {len(selected_rows)} 个章节吗？",
                QMessageBox.Yes | QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                return
        
        # 使用章节管理器删除章节
        deleted_count = self.chapter_manager.remove_chapters(selected_rows)
        self.safe_set_status(f"已删除 {deleted_count} 个章节")

    def jump_to_chapter(self, item):
        row = self.chapter_list.row(item)
        chapters = self.chapter_manager.chapters
        if 0 <= row < len(chapters):
            chapter = chapters[row]
            self.video_player.player.setPosition(chapter.time_ms)
            self.video_player.player.play()

    def show_chapter_context_menu(self, pos):
        """显示章节右键菜单"""
        item = self.chapter_list.itemAt(pos)
        if not item:
            return
        
        menu = QMenu(self)
        
        rename_action = menu.addAction("✏️ 重命名章节")
        delete_action = menu.addAction("🗑 删除章节")
        jump_action = menu.addAction("▶ 跳转到此章节")
        
        action = menu.exec(self.chapter_list.mapToGlobal(pos))
        
        if action == rename_action:
            self.rename_chapter_at_row(self.chapter_list.row(item))
        elif action == delete_action:
            self.delete_chapter()
        elif action == jump_action:
            self.jump_to_chapter(item)



    def rename_chapter_at_row(self, row):
        """重命名指定行的章节"""
        chapters = self.chapter_manager.chapters
        if 0 <= row < len(chapters):
            old_name = chapters[row].name
            new_name, ok = QInputDialog.getText(
                self, "重命名章节", "请输入新的章节名称:", text=old_name
            )
            if ok and new_name.strip():
                if self.chapter_manager.rename_chapter(row, new_name.strip()):
                    self.safe_set_status(f"章节已重命名为: {new_name.strip()}")
                else:
                    self.safe_set_status("重命名失败")

    def on_chapters_changed(self):
        """章节发生变化时的回调"""
        self.update_chapter_display()

    def save_chapters_to_video(self):
        if not self.video_path or not self.chapter_manager.chapters:
            self.safe_set_status("请先加载视频并添加章节！")
            return
        
        # 确保章节文件是最新的
        self.chapter_manager.save_to_txt()
        
        try:
            write_chapters(self.video_path)
            self.safe_set_status(f"章节写入完成: {os.path.basename(self.video_path)}")
        except Exception as e:
            self.safe_set_status(f"章节写入失败: {e}")

    def on_slider_pressed(self):
        self.is_slider_dragging = True

    def on_slider_released(self):
        self.is_slider_dragging = False
        pos = self.progress_slider.value() / 1000
        dur = self.video_player.player.duration()
        self.video_player.player.setPosition(int(dur * pos))

    def on_slider_moved(self, value):
        dur = self.video_player.player.duration()
        new_time = int(dur * (value / 1000))
        self.current_time_label.setText(self.format_time(new_time))
        self.video_player.player.setPosition(new_time)

    def update_total_time(self, duration):
        self.total_time_label.setText(self.format_time(duration))

    def update_progress(self):
        if not self.video_player.player.isAvailable() or self.is_slider_dragging:
            return
        pos = self.video_player.player.position()
        dur = self.video_player.player.duration()
        if dur > 0:
            new_value = int((pos / dur) * 1000)
            # 只在值发生变化时更新，减少不必要的UI刷新
            if self.progress_slider.value() != new_value:
                self.progress_slider.setValue(new_value)
            
            new_time_text = self.format_time(pos)
            if self.current_time_label.text() != new_time_text:
                self.current_time_label.setText(new_time_text)

    def format_time(self, ms):
        s = int(ms / 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        return f"{h:02}:{m:02}:{s:02}"

    def ms_to_chapter_time(self, ms):
        h, rem = divmod(ms // 1000, 3600)
        m, s = divmod(rem, 60)
        ms_rem = ms % 1000
        return f"{h:02}:{m:02}:{s:02}.{ms_rem:03}"

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                if url.isLocalFile() and (url.toLocalFile().lower().endswith('.mp4') or url.toLocalFile().lower().endswith('.mkv')):
                    event.acceptProposedAction()
                    return
        event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path.lower().endswith('.mp4') or file_path.lower().endswith('.mkv'):
                    self.load_video_file(file_path)
                    break

# ===== 工具函数: 判断对象是否已被删除 =====
def sip_is_deleted(obj):
    # PySide6: 检查对象是否已被删除，防止 RuntimeError
    try:
        return obj is None or getattr(obj, "parent", None) is None or obj.__bool__() is False
    except Exception:
        return True


