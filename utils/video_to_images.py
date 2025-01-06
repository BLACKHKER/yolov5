"""
@Author  ：Zhao
@Date    ： 14:22
@File    ：video_to_images.py
@Description: t按帧提取拍摄的视频保存为jpg图片，用来制作训练素材
@Version 1.0
"""

import os
import cv2
import time


def extract_frames(video_path, output_dir, frame_interval=60):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not video.isOpened():
        print("视频路径错误，或格式有误")
        return

    # 获取视频的总帧数
    total_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"总帧数: {total_frames}")

    # 获取视频文件名（去掉扩展名）
    video_filename = os.path.basename(video_path)  # 获取视频文件名
    video_name = os.path.splitext(video_filename)[0]  # 去掉扩展名

    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    frame_number = 0  # 遍历视频的帧
    saved_frame_count = 0   # 已保存的帧图片
    while True:
        ret, frame = video.read()

        # 如果读取失败，退出循环
        if not ret:
            break

        # 每隔指定的帧数保存一张图片
        if frame_number % frame_interval == 0:
            # 使用视频名和时间戳保证文件名唯一
            timestamp = int(time.time() * 1000)  # 毫秒级时间戳
            output_filename = os.path.join(output_dir, f"{video_name}_frame_{frame_number:04d}_{timestamp}.jpg")

            # 保存图片
            cv2.imwrite(output_filename, frame)
            saved_frame_count += 1
            print(f"保存视频的第 {frame_number} 帧图片到文件夹 {output_filename}")

        frame_number += 1

    # 释放视频捕捉对象
    video.release()
    print(f"保存了 {saved_frame_count} 个帧图片.")


if __name__ == "__main__":
    video_path = "../data/video/b.mp4"  # 视频路径/文件名
    output_dir = "../data/output_frames"  # 帧的输出目录
    frame_interval = 5  # 提取一张图片帧的帧间隔

    extract_frames(video_path, output_dir, frame_interval)
