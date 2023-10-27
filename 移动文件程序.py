# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-09-20
# @FileName: 移动文件程序.py
# 根据当前目录下的.mp3格式音频文件，将它们移动到指定目录下
import sys
import os
import shutil

# 创建目标目录
target_dir = "./NetEaseMusic/music"
os.makedirs(target_dir, exist_ok=True)

# 获取当前目录下的所有.mp3文件
current_dir = os.getcwd()
mp3_files = [file for file in os.listdir(current_dir) if file.endswith(".mp3")]

# 移动文件到目标目录
for file in mp3_files:
    shutil.move(file, os.path.join(target_dir, file))
    print(f"移动文件 {file} 到 {target_dir} 目录下")

print("移动完成")