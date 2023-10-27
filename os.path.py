# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-03-22
# @FileName: os.path.py
import os.path

"""
abspath  # 提供任何一个路径或文件名，会返回完整的路径名称
basename  # 返回路径名称的最后一个文件名或目录名称
dirname  # 返回指定路径名称的上层完整路径名称
exists  # 检查某一指定的路径或文件是否存在
getsize  # 返回指定文件的文件大小(Byte)
isabs  # 检查指定的路径是否为完整路径名称(绝对路径)
isfile  # 检查指定的路径是否为文件
isdir  # 检查指定的路径是否为目录
split  # 把绝对路径的文件和上层路径分开(取出文件名)
splitdrive  # 把绝对路径的磁盘驱动器和下层路径分开(取出磁盘驱动器)
join  # 把路径和文件名正确地结合成完整路径
"""
a=os.path.abspath("程序9-5.py")
print(a)

