import time
import numpy as np
import pygame

import Ai
import cp
import qz

#黑子
player = 1
color_p = pygame.Color(0, 0, 0)
#白子
AI = 2
color_A = pygame.Color(255, 255, 255)

#获取以毫秒为单位为的时间
t = pygame.time.get_ticks()  #该时间指的是从pygame初始化后开始计算，到调用该函数为止

#初始化创建及变量设置，默认调用
pygame.init()

#设置游戏窗口大小，宽长
width, height = 700, 700

#初始化显示窗口
screen = pygame.display.set_mode((width, height))

#设置显示窗口标题
pygame.display.set_caption("五子棋")

#棋盘数组
board = np.zeros((15, 15), dtype=int)
board_f = np.zeros((15, 15), dtype=int)

# 加载导入图片
sr = pygame.image.load("res\\qp.bmp")
screen.blit(sr, (0, 0))

image_defeat = pygame.image.load("res\\defeat.jpg")
image_peace = pygame.image.load("res\\peace.jpg")
image_win = pygame.image.load("res\\win.jpg")

scaled_image_defeat = pygame.transform.scale(image_defeat, (width, height))
scaled_image_peace = pygame.transform.scale(image_peace, (width, height))
scaled_image_win = pygame.transform.scale(image_win, (width, height))

#加载音频文件
pygame.mixer.music.load("res\\down.mp3")

#对显示窗口进行更新
pygame.display.flip()

#无限循环，直到python运行时退出结束
while True:
    #等待事件发生
    event = pygame.event.wait()
    #检查事件的类型并进行相应处理
    if event.type == pygame.QUIT:
        #如果事件为退出事件，则退出程序
        exit('成功退出')

    if event.type == pygame.MOUSEBUTTONDOWN:
        #print('鼠标按下', event.pos)
        # 获取鼠标点击位置
        mouse_x, mouse_y = event.pos
        #计算落子位置
        p_x = (mouse_x - 13) // 45
        p_y = (mouse_y - 13) // 45
        if board[p_y][p_x] != 0:
            continue

        #落子
        board[p_y][p_x] = player

        #绘制棋子
        qz.draw_piece(screen, p_x, p_y, color_p)
        pygame.mixer.music.play(0)
        pygame.display.update()
        #print('玩家落子', p_x, p_y, board[p_y][p_x])

        if event.type == pygame.MOUSEBUTTONUP:
            print('鼠标弹起')
            pass
        if cp.qt(board, player) == 1:
            screen.fill((0, 0, 0))
            screen.blit(scaled_image_win, (0, 0))
            time.sleep(5)
            pygame.display.update()
            time.sleep(5)
            exit()

        elif cp.qt(board, player) == 2:
            screen.fill((0, 0, 0))
            screen.blit(scaled_image_peace, (0, 0))
            time.sleep(5)
            pygame.display.update()
            time.sleep(5)
            exit()

        time.sleep(1)

        #AI落子
        while True:
            a_x, a_y = Ai.lz(board, board_f, p_x, p_y)
            if board[a_x][a_y] == 0:
                break
        '''while True:
            a_x = random.randint(0, 14)
            a_y = random.randint(0, 14)
            if board[a_y][a_x]==0:break'''
        board[a_x][a_y] = AI
        qz.draw_piece(screen, a_y, a_x, color_A)
        pygame.mixer.music.play(0)
        #print('AI落子', a_x, a_y, board[a_y][a_x])
        #print(board_f)

        pygame.display.update()

        if cp.qt(board, AI) == 1:
            screen.fill((0, 0, 0))
            screen.blit(scaled_image_defeat, (0, 0))
            time.sleep(5)
            pygame.display.update()
            time.sleep(5)
            exit()

        elif cp.qt(board, AI) == 2:
            screen.fill((0, 0, 0))
            screen.blit(scaled_image_peace, (0, 0))
            time.sleep(5)
            pygame.display.update()
            time.sleep(5)
            exit()
