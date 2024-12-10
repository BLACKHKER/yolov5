"""
@Author  ：Zhao
@Date    ： 14:22
@File    ：video_to_images.py
@Description: t按帧提取视频保存为jpg图片，拍摄训练素材用
@Version 1.0
"""

import os
import cv2

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

    # 创建一个新的文件夹，避免覆盖
    video_filename = os.path.basename(video_path)  # 获取视频文件名（带扩展名）
    video_name = os.path.splitext(video_filename)[0]  # 去掉扩展名
    video_output_dir = os.path.join(output_dir, video_name)  # 用视频名作为文件夹名

    if not os.path.exists(video_output_dir):
        os.makedirs(video_output_dir)

    # 遍历视频的帧
    frame_number = 0
    saved_frame_count = 0

    while True:
        # 如果读取失败，退出循环
        ret, frame = video.read()
        if not ret:
            break

        # 每隔指定的帧数保存一张图片
        if frame_number % frame_interval == 0:
            # 生成图片文件名
            output_filename = os.path.join(video_output_dir, f"frame_{frame_number:04d}.jpg")
            # 保存图片
            cv2.imwrite(output_filename, frame)
            saved_frame_count += 1
            print(f"保存视频的第 {frame_number} 帧图片到文件夹 {output_filename}")
        frame_number += 1

    # 释放视频捕捉对象
    video.release()
    print(f"保存了 {saved_frame_count} 个帧图片.")

if __name__ == "__main__":
    video_path = "../data/video/IMG_5001.mp4"  # 视频路径/文件名
    output_dir = "../data/output_frames"   # 帧的输出目录
    frame_interval = 5  # 提取一张图片帧的帧间隔

    extract_frames(video_path, output_dir, frame_interval)
