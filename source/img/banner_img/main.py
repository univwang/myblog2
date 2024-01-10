import os
import shutil

def rename_and_move_files():
    folder_path = os.getcwd()  # 获取当前目录
    new_folder_path = os.path.join(folder_path, "renamed_files")
    os.makedirs(new_folder_path, exist_ok=True)

    jpg_files = [file for file in os.listdir(folder_path) if file.lower().endswith('.jpg')]

    if not jpg_files:
        print(f"当前目录 '{folder_path}' 中没有jpg文件。")
        return

    for index, jpg_file in enumerate(jpg_files, start=1):
        old_path = os.path.join(folder_path, jpg_file)
        filename, extension = os.path.splitext(jpg_file)
        new_name = f"{index}{extension}"
        new_path = os.path.join(new_folder_path, new_name)

        count = 1
        while os.path.exists(new_path):
            new_name = f"{index}_{count}{extension}"
            new_path = os.path.join(new_folder_path, new_name)
            count += 1

        shutil.copy(old_path, new_path)
        print(f"已将文件 '{jpg_file}' 重命名为 '{new_name}' 并移动到新文件夹。")

    for jpg_file in jpg_files:
        file_path = os.path.join(folder_path, jpg_file)
        os.remove(file_path)

    new_files = os.listdir(new_folder_path)
    for new_file in new_files:
        new_file_path = os.path.join(new_folder_path, new_file)
        shutil.move(new_file_path, folder_path)

    os.rmdir(new_folder_path)

if __name__ == "__main__":
    rename_and_move_files()
