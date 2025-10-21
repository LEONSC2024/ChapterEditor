# video_player.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QFileDialog
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Qt, Signal, Slot, QUrl


class VideoPlayer(QWidget):
    # 自定义信号：外部主窗口用来更新进度条
    position_changed = Signal(int)
    duration_changed = Signal(int)

    def __init__(self):
        super().__init__()

        # 视频播放核心
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        # 视频显示窗口
        self.video_widget = QVideoWidget()
        self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.player.setVideoOutput(self.video_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)
        self.setLayout(layout)

        # 连接信号
        self.player.positionChanged.connect(self.position_changed.emit)
        self.player.durationChanged.connect(self.duration_changed.emit)

        # 当前播放文件路径
        self.current_file = None

        # 确保窗口可以接收键盘事件
        self.setFocusPolicy(Qt.StrongFocus)
        self.video_widget.setFocusPolicy(Qt.NoFocus)

    @Slot()
    def open_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "选择视频文件", "", "视频文件 (*.mp4 *.mkv *.mov *.avi)"
        )
        if file:
            self.load_video(file)

    def load_video(self, file_path):
        """加载视频文件并播放"""
        self.current_file = file_path
        self.player.setSource(QUrl.fromLocalFile(file_path))
        self.player.play()

    def toggle_play(self):
        """播放/暂停切换"""
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def seek_relative(self, seconds: float):
        """快进/快退，单位秒"""
        new_pos = self.player.position() + int(seconds * 1000)
        new_pos = max(0, min(new_pos, self.player.duration()))
        self.player.setPosition(new_pos)

    def set_position(self, position: int):
        """拖动进度条时设置播放位置"""
        self.player.setPosition(position)

    def set_playback_rate(self, rate: float):
        """设置倍速播放"""
        self.player.setPlaybackRate(rate)

    def current_position(self) -> int:
        """返回当前播放位置（毫秒）"""
        return self.player.position()

    def keyPressEvent(self, event):
        """处理快捷键：空格播放/暂停，左右快进/快退10秒"""
        key = event.key()
        if key == Qt.Key_Space:
            self.toggle_play()
            event.accept()
        elif key == Qt.Key_Left:
            self.seek_relative(-10)
            event.accept()
        elif key == Qt.Key_Right:
            self.seek_relative(10)
            event.accept()
        else:
            super().keyPressEvent(event)