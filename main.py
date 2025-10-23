# 程序入口

from PySide6.QtWidgets import QApplication
from main_window import MainWindow
import sys


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("MP4章节封面编辑器")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())