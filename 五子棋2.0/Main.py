import tkinter as tk

import Gui

if __name__ == '__main__':
    # 创建主窗口和登录页面
    root = tk.Tk()
    Gui.LoginPage(root).page()
    root.mainloop()
