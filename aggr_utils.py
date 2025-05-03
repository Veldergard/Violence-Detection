import platform
import os
import shutil


def print_system_info():
    """Вывод информации о системе"""
    print(f"Operating System: {platform.platform()}")
    print(f"Python version: {platform.python_version()}")


def ensure_dir_exists(dir_path):
    """
    Создает директорию, если она не существует.
    """
    os.makedirs(dir_path, exist_ok=True)


def clear_directory(dir_path):
    """
    Очищает содержимое директории.
    """
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # удаляем файлы и симлинки
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # удаляем поддиректории
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")
