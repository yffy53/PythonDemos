import numpy as np
import pygame
import time

import Draw


#获取以毫秒为单位为的时间
gl_t = pygame.time.get_ticks()  #该时间指的是从pygame初始化后开始计算，到调用该函数为止

#初始化创建及变量设置，默认调用
pygame.init()

#设置游戏窗口大小，宽长
gl_width, gl_height = 700, 700

#初始化显示窗口
gl_screen = pygame.display.set_mode((gl_width, gl_height))

#设置显示窗口标题
pygame.display.set_caption("五子棋")

#设置字体
font = pygame.font.Font('res\\simsun.ttc', 100)

#渲染文本
string_win = font.render('此胜当赏', True, 'red')
string_defeat = font.render('菜就多练', True, 'green')
string_peace = font.render('平分秋色', True, 'blue')

# 加载导入图片
gl_sr = pygame.image.load("res\\qp.bmp")

image_chess_black = pygame.image.load("res\\chess_black.png")
image_chess_white = pygame.image.load("res\\chess_white.png")

scaled_image_chess_black = pygame.transform.scale(image_chess_black, (50, 50))
scaled_image_chess_white = pygame.transform.scale(image_chess_white, (50, 50))

#加载音频文件
pygame.mixer.music.load("res\\down.mp3")


class Board:
    def __init__(self):
        #棋盘数据
        self.board_data = np.zeros((15, 15), dtype=int)
        #悔棋棋盘
        self.board_back = np.zeros((15, 15), dtype=int)

    def __getitem__(self, index):
        return self.board_data[index]  #实现对象索引访问

    #显示棋盘
    def show_board(self):
        gl_screen.fill((0, 0, 0))  #清屏
        gl_screen.blit(gl_sr, (0, 0))  #加载棋盘
        #根据棋盘数组绘制棋子
        for i in range(15):
            for j in range(15):
                if self.board_back[i, j] == 1:
                    Draw.draw_piece(i, j, 1)
                elif self.board_back[i, j] == -1:
                    Draw.draw_piece(i, j, -1)
        #对显示窗口进行更新
        pygame.display.flip()

    #指定落子位置
    def move_down(self, x, y, chess, name='电脑'):
        if self.board_data[x][y] != 0:  #该位置已有棋子
            return False
        else:
            if name == '玩家':
                np.copyto(self.board_back, self.board_data)
            self.board_data[x][y] = chess
            Draw.draw_chartlet(x, y, chess)
            pygame.mixer.music.play(0)  #播放落子音效
            pygame.display.update()
            return True

    #悔棋
    def move_back(self):
        np.copyto(self.board_data, self.board_back)  #棋盘和悔棋棋盘同步数据
        self.show_board()

    #是否平局
    def is_draw(self):
        #判断棋盘中所有元素是否都不等于0
        return all(all(cell != 0 for cell in row) for row in self.board_data)

    #平局画面
    @staticmethod
    def draw_draw():
        gl_screen.blit(string_peace, (gl_width / 4 - 20, gl_height / 2))
        time.sleep(3)
        pygame.display.update()

    #是否获胜
    def is_win(self, chess):
        # 横向检查
        for row in range(15):
            for col in range(11):
                if all(self.board_data[row][col + i] == chess for i in range(5)):
                    return True

        # 纵向检查
        for col in range(15):
            for row in range(11):
                if all(self.board_data[row + i][col] == chess for i in range(5)):
                    return True

        # 检查主对角线
        for row in range(11):
            for col in range(11):
                if all(self.board_data[row + i][col + i] == chess for i in range(5)):
                    return True

        # 检查副对角线
        for row in range(11):
            for col in range(4, 15):
                if all(self.board_data[row + i][col - i] == chess for i in range(5)):
                    return True

        return False

    #胜负已分
    @staticmethod
    def win_draw(player):
        if player.name == '玩家':
            string = string_win
        else:
            string = string_defeat
        gl_screen.blit(string, (gl_width / 4 - 20, gl_height / 2))
        pygame.display.update()

    #重置棋盘
    def reset_board(self):
        self.board_data = np.zeros((15, 15), dtype=int)
        self.board_back = np.zeros((15, 15), dtype=int)
        self.show_board()
