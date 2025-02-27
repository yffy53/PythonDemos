import tkinter as tk
from tkinter import messagebox

import Login
import Game


class LoginPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master  #传入界面
        self.password_entry = None
        self.second_window = None
        self.username_entry = None

    def page(self):
        self.master.title('登录页面')

        title_label = tk.Label(self.master, text="登录页面")
        title_label.pack()

        username_label = tk.Label(self.master, text="用户名:")
        username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        password_label = tk.Label(self.master, text="密码:")
        password_label.pack()
        self.password_entry = tk.Entry(self.master, show='*')
        self.password_entry.pack()

        login_button = tk.Button(self.master, text="登录", command=self.login)  #按钮跳转至self.login函数
        login_button.pack()

        register_button = tk.Button(self.master, text="注册", command=self.registration)
        register_button.pack()

        lose_button = tk.Button(self.master, text="忘记密码", command=self.lose)
        lose_button.pack()

    def login(self):
        #获取输入的用户名，密码
        username = self.username_entry.get()
        password = self.password_entry.get()
        if Login.fetch_contrast(username, password) == 1:
            messagebox.showinfo("成功", "登录成功！")  #弹出提示框
            self.master.destroy()  #关闭登录窗口
            Login.username_now = username
            Login.password_now = password
            Game.Game().start()  #开始游戏
        else:
            messagebox.showerror("错误", "用户名或密码错误！")

    def registration(self):  #打开注册窗口
        self.second_window = tk.Toplevel(self.master)  # 创建Toplevel窗口作为第二个窗口
        RegisterPage(self.second_window)
        #self.master.withdraw()  # 隐藏当前窗口

    def lose(self):  #打开修改密码窗口
        self.second_window = tk.Toplevel(self.master)
        ForgetPassword(self.second_window)


class RegisterPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title('注册页面')

        self.title_label = tk.Label(self.master, text="注册页面")
        self.title_label.pack()

        # 添加注册页面所需的控件，用户名、密码输入框和注册按钮等
        self.username_label = tk.Label(self.master, text="用户名:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="密码:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show='*')
        self.password_entry.pack()

        self.register_button = tk.Button(self.master, text="注册", command=self.close_window)
        self.register_button.pack()

    def close_window(self):  #注册用户
        username = self.username_entry.get()
        password = self.password_entry.get()
        if Login.fetch_contrast(username, password) == 3:
            Login.write_dict_a(username, password)
        else:
            messagebox.showerror("错误", '用户名已存在')
        self.master.destroy()  # 关闭当前窗口，通常会自动返回到之前的窗口（如果之前窗口没有被销毁）


class ForgetPassword(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.title('忘记密码')

        self.title_label = tk.Label(self.master, text="忘记密码")
        self.title_label.pack()

        self.password_label_admin = tk.Label(self.master, text="管理员密码:")
        self.password_label_admin.pack()
        self.password_entry_admin = tk.Entry(self.master, show='*')
        self.password_entry_admin.pack()

        self.username_label = tk.Label(self.master, text="用户名:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()

        self.password_label = tk.Label(self.master, text="新密码:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show='*')
        self.password_entry.pack()

        self.register_button = tk.Button(self.master, text="更改", command=self.reset)
        self.register_button.pack()

    def reset(self):  #修改密码
        admin = self.password_entry_admin.get()
        username = self.username_entry.get()
        password_new = self.password_entry.get()
        if admin == Login.password_max:  #管理员密码正确
            if Login.write_dict_w(username, password_new) == 1:  #用户名存在
                messagebox.showinfo("成功", '密码更改成功')
            else:
                messagebox.showerror("错误", '用户名不存在')
        else:
            messagebox.showerror("错误", '管理员密码错误')
