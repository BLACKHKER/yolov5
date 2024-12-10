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

    # 创建输出文件夹（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 遍历视频的帧
    frame_number = 0
    # 已保存的图片张数
    saved_frame_count = 0

    while True:
        ret, frame = video.read()

        # 如果读取失败，退出循环
        if not ret:
            break

        # 每隔指定的帧数保存一张图片
        if frame_number % frame_interval == 0:
            # 生成图片文件名
            output_filename = os.path.join(output_dir, f"frame_{frame_number:04d}.jpg")
            # 保存图片
            cv2.imwrite(output_filename, frame)
            saved_frame_count += 1
            print(f"Saved frame {frame_number} as {output_filename}")

        frame_number += 1

    # 释放视频捕捉对象
    video.release()
    print(f"Extracted {saved_frame_count} frames.")

if __name__ == "__main__":
    video_path = "../data/video/IMG_4982.mp4"  # 视频路径/文件名
    output_dir = "../data/output_frames"   # 帧的输出目录
    frame_interval = 20  # 每60帧提取一张图片

    extract_frames(video_path, output_dir, frame_interval)
