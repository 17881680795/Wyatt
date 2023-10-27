# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-16
# @FileName: 脚本：数据批量化标注.py
import os
from PIL import Image, ImageTk
from tkinter import Tk, filedialog, messagebox
from tkinter import StringVar, OptionMenu, Label, Button

# 标注类别
class_labels = ['cat', 'dog', 'horse']


# 批量标注主函数
def batch_annotation():
    # 选择文件夹
    folder = filedialog.askdirectory(title='Select folder')
    if folder == '':
        return

    # 遍历文件夹中的所有图片
    for file in os.listdir(folder):
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):

            # 显示图片
            img = Image.open(os.path.join(folder, file))
            img_tk = ImageTk.PhotoImage(img)
            label_img.config(image=img_tk)
            label_img.image = img_tk

            # 等待用户选择类别
            chosen_label.set('')
            while chosen_label.get() == '':
                window.update()

            # 保存标注结果
            label = chosen_label.get()
            with open(os.path.join(folder, file[:-4] + '.txt'), mode='w') as f:
                f.write(label)

            # 清空选择
            chosen_label.set('')

    # 完成
    messagebox.showinfo('Batch Annotation', 'Batch annotation completed.')


# 创建图形界面
window = Tk()

# 创建选择类别的下拉列表
chosen_label = StringVar(window)
chosen_label.set(class_labels[0])  # 默认选择第一个类别
option_menu = OptionMenu(window, chosen_label, *class_labels)
option_menu.pack()

# 创建显示图像的标签
label_img = Label(window)
label_img.pack()

# 创建批量标注按钮
btn_batch_annotation = Button(window, text="Batch Annotation", command=batch_annotation)
btn_batch_annotation.pack()

# 启动图形界面
window.mainloop()
