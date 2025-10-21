import shutil
import subprocess
import sys
import os

# 项目根目录与相关路径
project_dir = "/Users/08-软件插件/MP4章节封面编辑器"
entry_script = os.path.join(project_dir, "main1.0.py")
icon_path = os.path.join(project_dir, "icon.icns")
dist_name = "MP4章节封面编辑器"

def clean_build_artifacts():
    """自动清理旧的 dist、build、spec 文件。"""
    targets = [
        os.path.join(project_dir, "dist"),
        os.path.join(project_dir, "build"),
        os.path.join(project_dir, f"{dist_name}.spec"),
    ]
    for target in targets:
        if os.path.isdir(target):
            print(f"正在删除目录: {target}")
            shutil.rmtree(target, ignore_errors=True)
        elif os.path.isfile(target):
            print(f"正在删除文件: {target}")
            os.remove(target)

def check_icon():
    """检查图标文件是否存在，不存在则警告并返回None。"""
    if not os.path.exists(icon_path):
        print(f"警告: 图标文件不存在: {icon_path}")
        print("将使用默认图标打包。")
        return None
    return icon_path

def build_app():
    """
    使用 PyInstaller 打包 macOS ARM64 应用，显式收集 QtMultimedia、platforms 插件，并设置 QT_PLUGIN_PATH。
    """
    icon_arg = check_icon()

    # PySide6 Qt 插件目录
    qt_plugins_dir = os.path.join(sys.prefix, "lib", f"python{sys.version_info.major}.{sys.version_info.minor}", "site-packages", "PySide6", "Qt", "plugins")
    multimedia_plugins = os.path.join(qt_plugins_dir, "multimedia")
    platforms_plugins = os.path.join(qt_plugins_dir, "platforms")

    # 设置 QT_PLUGIN_PATH 环境变量
    env = os.environ.copy()
    env["QT_PLUGIN_PATH"] = qt_plugins_dir

    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name", dist_name,
        "--windowed",
        "--clean",
        "--add-data", f"{multimedia_plugins}:PySide6/Qt/plugins/multimedia",
        "--add-data", f"{platforms_plugins}:PySide6/Qt/plugins/platforms",
        entry_script
    ]
    if icon_arg:
        cmd.insert(5, f"--icon={icon_arg}")
    print("执行命令:", " ".join(cmd))
    try:
        subprocess.run(cmd, check=True, env=env)
        print(f"\n打包完成！可执行程序在 {os.path.join(project_dir, 'dist', dist_name + '.app')}")
    except Exception as e:
        print(f"打包失败: {e}")

if __name__ == "__main__":
    try:
        clean_build_artifacts()
        build_app()
    except Exception as err:
        print(f"发生异常: {err}")