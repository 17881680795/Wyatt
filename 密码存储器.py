# -*- coding:utf-8 -*-
# @Auther:    Wyatt
# @Date:     2023-04-19
# @FileName: 密码存储器.py
import tkinter as tk
import random
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Password Generator")

        # 密码生成器部分
        password_frame = tk.Frame(self.root)
        password_frame.pack(pady=20)

        password_label = tk.Label(password_frame, text="Password: ", font=("Helvetica", 14))
        password_label.grid(row=0, column=0, padx=(10, 0))

        self.password_entry = tk.Entry(password_frame, font=("Helvetica", 14), width=20)
        self.password_entry.grid(row=0, column=1)

        password_button = tk.Button(password_frame, text="Generate Password", command=self.generate_password)
        password_button.grid(row=1, column=0, columnspan=2, pady=(10, 0))
        # 自动填充表单部分
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)

        name_label = tk.Label(form_frame, text="Name: ", font=("Helvetica", 14))
        name_label.grid(row=0, column=0)

        self.name_entry = tk.Entry(form_frame, font=("Helvetica", 14), width=20)
        self.name_entry.insert(tk.END, "Wyatt")
        self.name_entry.grid(row=0, column=1)
        email_label = tk.Label(form_frame, text="Email: ", font=("Helvetica", 14))
        email_label.grid(row=1, column=0, pady=(10, 0))

        self.email_entry = tk.Entry(form_frame, font=("Helvetica", 14), width=20)
        self.email_entry.insert(tk.END, "13794190771@139.com")
        self.email_entry.grid(row=1, column=1, pady=(10, 0))
        password_label = tk.Label(form_frame, text="Password: ", font=("Helvetica", 14))
        password_label.grid(row=2, column=0, pady=(10, 0))

        password_button = tk.Button(form_frame, text="Fill Form", command=self.fill_form)
        password_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        # 截屏保护
        self.root.bind("<Control-c>", self.protect_screenshot)

    def generate_password(self):
        password_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
        password_length = 20
        password = "".join(random.choice(password_chars) for i in range(password_length))
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)

    def fill_form(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        form = f"Name: {name}\nEmail: {email}\nPassword: {password}"
        # 将表单信息复制到剪切板
        self.root.clipboard_clear()
        self.root.clipboard_append(form)

    def protect_screenshot(self, event=None):
        self.root.withdraw()
        self.root.deiconify()


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
