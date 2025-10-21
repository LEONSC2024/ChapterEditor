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
import json
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QFileDialog, QComboBox, QListWidget, QMessageBox, QSplitter, QSlider
)
from PySide6.QtCore import Qt, QTimer
from video_player import VideoPlayer
from mp4_writer import write_chapters

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("🎬 MP4章节封面编辑器")
        self.setGeometry(200, 100, 1200, 750)
        self.setAcceptDrops(True)

        self.video_path = None
        self.previous_video_path = None  # 记录上一个视频路径
        self.chapters = []
        self.is_slider_dragging = False

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

        self.speed_label = QLabel("倍速：")
        self.speed_box = QComboBox()
        self.speed_box.addItems(["1.0x", "1.25x", "1.5x", "2.0x", "3.0x", "4.0x"])
        self.speed_box.currentTextChanged.connect(self.change_speed)
        control_layout.addWidget(self.speed_label)
        control_layout.addWidget(self.speed_box)

        # 主题切换
        self.theme_label = QLabel("主题：")
        self.theme_box = QComboBox()
        self.theme_box.addItems(["深灰", "浅白"])
        self.theme_box.currentTextChanged.connect(self.set_theme)
        control_layout.addWidget(self.theme_label)
        control_layout.addWidget(self.theme_box)

        self.save_button = QPushButton("💾 保存章节到视频")
        self.save_button.clicked.connect(self.save_chapters_to_video)
        control_layout.addWidget(self.save_button)
        control_layout.addStretch()

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

        # 定时器同步进度条
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(500)

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
        # QComboBox 样式表（深灰/浅白），统一渲染，去除选中项勾选符号，文字靠左，设置宽度和下拉项高度
        if theme_name == "深灰":
            self.setStyleSheet(DARK_THEME)
            combo_style = """
            QComboBox {
                padding-left: 10px;
                border-radius: 6px;
                background: #2d3136;
                color: #e0e0e0;
                border: 1px solid #444;
                min-height: 28px;
                min-width: 40px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background: #2d3136;
                color: #e0e0e0;
                border-radius: 6px;
                selection-background-color: #3a99fc;
                selection-color: #fff;
            }
            QComboBox::item:selected:!hover {
                /* 不显示勾选符号 */
            }
            QComboBox QAbstractItemView::item:selected::indicator {
                width: 0px;
                height: 0px;
            }
            QComboBox QAbstractItemView::item {
                padding-left: 6px;
                min-height: 24px;
            }
            """
        else:
            self.setStyleSheet(LIGHT_THEME)
            combo_style = """
            QComboBox {
                padding-left: 6px;
                border-radius: 6px;
                background: #fff;
                color: #222;
                border: 1px solid #d3d3d3;
                min-height: 28px;
                min-width: 80px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox QAbstractItemView {
                background: #fff;
                color: #222;
                border-radius: 6px;
                selection-background-color: #3a99fc;
                selection-color: #fff;
            }
            QComboBox::item:selected:!hover {
                /* 不显示勾选符号 */
            }
            QComboBox QAbstractItemView::item:selected::indicator {
                width: 0px;
                height: 0px;
            }
            QComboBox QAbstractItemView::item {
                padding-left: 6px;
                min-height: 24px;
            }
            """
        # 动态调整 QComboBox 的样式
        self.speed_box.setStyleSheet(combo_style)
        self.theme_box.setStyleSheet(combo_style)

    def closeEvent(self, event):
        if self.video_path:
            base_name = os.path.splitext(os.path.basename(self.video_path))[0]
            txt_path = os.path.join(os.path.dirname(self.video_path), f"{base_name}_chapters.txt")
            try:
                if os.path.exists(txt_path):
                    os.remove(txt_path)
                    print(f"已删除章节文件: {txt_path}")
            except Exception as e:
                print(f"删除章节文件失败: {e}")
        super().closeEvent(event)

    def safe_set_status(self, text):
        # 避免在窗口关闭后操作已删除对象
        if hasattr(self, "status_label") and self.status_label and not sip_is_deleted(self.status_label):
            QTimer.singleShot(0, lambda: self.status_label.setText(text))

    def change_speed(self, text):
        try:
            speed = float(text.replace('x', ''))
            self.video_player.player.setPlaybackRate(speed)
            self.safe_set_status(f"倍速已设置为 {speed}x")
        except Exception as e:
            self.safe_set_status(f"设置倍速失败: {e}")

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

        # 删除上一个视频的 TXT
        if self.previous_video_path:
            old_base = os.path.splitext(os.path.basename(self.previous_video_path))[0]
            old_dir = os.path.dirname(self.previous_video_path)
            old_txt = os.path.join(old_dir, f"{old_base}_chapters.txt")
            if os.path.isfile(old_txt):
                try:
                    os.remove(old_txt)
                    print(f"已删除旧章节文件: {old_txt}")
                except Exception as e:
                    print(f"删除旧章节文件失败: {e}")

        # 更新路径
        self.previous_video_path = file_path
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
        if not self.load_chapters_from_video(file_path):
            self.load_chapters_from_txt(file_path)

    # ===== 从视频读取章节 =====
    def load_chapters_from_video(self, video_path):
        try:
            cmd = ["ffprobe", "-v", "error", "-print_format", "json", "-show_chapters", video_path]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            data = json.loads(result.stdout)
            chapters = data.get("chapters", [])

            if not chapters:
                return False

            self.chapters.clear()
            self.chapter_list.clear()
            # 先读取所有章节
            temp_chapters = []
            for idx, ch in enumerate(chapters, start=1):
                start_time = float(ch.get("start_time", 0))
                ms = int(start_time * 1000)
                name = ch.get("tags", {}).get("title", f"Chapter {idx}")
                temp_chapters.append({"name": name, "time_ms": ms})
            # 按时间升序排序
            temp_chapters.sort(key=lambda c: c["time_ms"])
            self.chapters = temp_chapters
            # 显示时用顺序编号
            for idx, c in enumerate(self.chapters, start=1):
                display_time = self.ms_to_chapter_time(c["time_ms"])
                self.chapter_list.addItem(f"{idx:02}. {display_time} - {c['name']}")

            self.update_chapters_txt()
            # self.export_chapters_to_xml()  # 不再导入视频时生成XML文件
            return True
        except Exception as e:
            self.safe_set_status(f"读取视频章节失败: {e}")
            return False

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

    # ===== 以下其他方法保持原逻辑 =====
    def load_chapters_from_txt(self, video_path):
        base_name = os.path.splitext(os.path.basename(video_path))[0]
        txt_path = os.path.join(os.path.dirname(video_path), f"{base_name}_chapters.txt")
        self.chapters.clear()
        self.chapter_list.clear()
        if not os.path.exists(txt_path):
            return
        try:
            with open(txt_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            temp = {}
            for line in lines:
                line = line.strip()
                if line.startswith("CHAPTER") and "=" in line and "NAME" not in line:
                    key, value = line.split("=", 1)
                    num = key[7:9]
                    temp[num] = {"time_str": value, "name": None}
                elif line.startswith("CHAPTER") and "NAME=" in line:
                    key, value = line.split("=", 1)
                    num = key[7:9]
                    if num in temp:
                        temp[num]["name"] = value
            keys_sorted = sorted(temp.keys())
            for idx, k in enumerate(keys_sorted, start=1):
                t = temp[k]
                ms = self.parse_chapter_time(t["time_str"])
                name = t["name"] if t["name"] is not None else f"Chapter {idx}"
                self.chapters.append({"name": name, "time_ms": ms})
                display_time = self.ms_to_chapter_time(ms)
                self.chapter_list.addItem(f"{display_time} - {name}")
        except Exception as e:
            self.safe_set_status(f"无法读取章节TXT: {e}")

    def parse_chapter_time(self, line):
        try:
            if "." in line:
                hhmmss, ms = line.split(".")
                ms = int(ms)
            else:
                hhmmss = line
                ms = 0
            h, m, s = map(int, hhmmss.split(":"))
            total_ms = ((h * 60 + m) * 60 + s) * 1000 + ms
            return total_ms
        except Exception:
            return 0

    def update_chapters_txt(self):
        # 清理上一个视频的 TXT 文件
        if hasattr(self, 'previous_video_path') and self.previous_video_path and self.previous_video_path != self.video_path:
            old_base = os.path.splitext(os.path.basename(self.previous_video_path))[0]
            old_dir = os.path.dirname(self.previous_video_path)
            old_txt = os.path.join(old_dir, f"{old_base}_chapters.txt")
            if os.path.isfile(old_txt):
                try:
                    os.remove(old_txt)
                    print(f"已删除旧章节文件: {old_txt}")
                except Exception as e:
                    print(f"删除旧章节文件失败: {e}")

        # 更新 previous_video_path
        self.previous_video_path = self.video_path

        if not self.video_path or not self.chapters:
            return

        # 按时间升序排序章节
        self.chapters.sort(key=lambda c: c["time_ms"])

        base_name = os.path.splitext(os.path.basename(self.video_path))[0]
        txt_path = os.path.join(os.path.dirname(self.video_path), f"{base_name}_chapters.txt")
        try:
            self.chapter_list.clear()
            # 先清空TXT文件
            with open(txt_path, "w", encoding="utf-8"):
                pass
            # 逐一写入章节（顺序编号，固定两位数字）
            for idx, c in enumerate(self.chapters, start=1):
                ms_total = c["time_ms"]
                h, rem = divmod(ms_total // 1000, 3600)
                m, s = divmod(rem, 60)
                ms_rem = ms_total % 1000
                time_str = f"{h:02}:{m:02}:{s:02}.{ms_rem:03}"
                with open(txt_path, "a", encoding="utf-8") as f:
                    f.write(f"CHAPTER{idx:02}={time_str}\n")
                    f.write(f"CHAPTER{idx:02}NAME={c['name']}\n")
                self.chapter_list.addItem(f"{idx:02}. {time_str} - {c['name']}")
        except Exception as e:
            self.safe_set_status(f"保存章节TXT失败: {e}")

    def add_chapter(self):
        if not self.video_path:
            self.safe_set_status("请先加载视频！")
            return
        current_time = self.video_player.player.position()
        name = f"Chapter {len(self.chapters)+1}"  # 原始名称
        self.chapters.append({"name": name, "time_ms": current_time})
        self.update_chapters_txt()  # 自动刷新显示为 01, 02...
        self.safe_set_status(f"已添加章节：{name}")

    def delete_chapter(self):
        selected_rows = [self.chapter_list.row(item) for item in self.chapter_list.selectedItems()]
        if not selected_rows:
            QMessageBox.warning(self, "提示", "请先选择要删除的章节。")
            return
        # 删除章节时，按索引从大到小删除，避免索引混乱
        selected_rows.sort(reverse=True)
        for row in selected_rows:
            self.chapters.pop(row)
            self.chapter_list.takeItem(row)
        # 自动选择上一个或下一个章节
        if selected_rows[0] < len(self.chapters):
            self.chapter_list.setCurrentRow(selected_rows[0])
        elif len(self.chapters) > 0:
            self.chapter_list.setCurrentRow(len(self.chapters)-1)
        # 更新 TXT 刷新显示
        self.update_chapters_txt()

    def jump_to_chapter(self, item):
        row = self.chapter_list.row(item)
        chapter = self.chapters[row]
        self.video_player.player.setPosition(chapter["time_ms"])
        self.video_player.player.play()

    def save_chapters_to_video(self):
        if not self.video_path or not self.chapters:
            self.safe_set_status("请先加载视频并添加章节！")
            return
        self.update_chapters_txt()
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
            self.progress_slider.setValue(int((pos / dur) * 1000))
            self.current_time_label.setText(self.format_time(pos))

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


