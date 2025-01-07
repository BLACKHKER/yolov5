import os
import time

# 设置目标文件夹路径
folder_path = 'C:/Users/Zhao/Desktop/my/labelimg/JPEGImages'  # 替换为你的文件夹路径

# 遍历文件夹中的所有文件
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    # 检查是否是文件（跳过文件夹）
    if os.path.isfile(file_path):
        # 提取文件名和扩展名
        name, ext = os.path.splitext(filename)

        # 在原始文件名中查找前缀部分，并拼接新的文件名
        # 假设文件名格式为 "a_frame_0015_XXXX.txt"，需要提取前缀到最后一个下划线
        prefix = "_".join(name.split('_')[:-1])  # 获取文件名前缀（如 "a_frame_0015"）

        # 生成新的文件名
        new_filename = f"{prefix}{ext}"

        # 拼接新的文件路径
        new_file_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(file_path, new_file_path)

        # 打印旧文件名和新文件名
        print(f"已重命名: {filename} -> {new_filename}")
