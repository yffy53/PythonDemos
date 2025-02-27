#绘制棋子
import pygame


def draw_piece(screen, x, y, color):
    #根据落子位置计算棋子中心
    center_x = 35 + 45 * x
    center_y = 35 + 45 * y

    #绘制棋子
    pygame.draw.circle(screen, color, (center_x, center_y), 18)
