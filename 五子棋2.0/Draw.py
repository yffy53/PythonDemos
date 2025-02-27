import pygame

import Board


def draw_piece(x, y, chess):
    #根据落子位置计算棋子中心
    center_x = 35 + 45 * x
    center_y = 35 + 45 * y

    #棋子颜色
    if chess == 1:
        color = pygame.Color(0, 0, 0)
    else:
        color = pygame.Color(255, 255, 255)

    #绘制棋子
    pygame.draw.circle(Board.gl_screen, color, (center_x, center_y), 18)


def draw_chartlet(x, y, chess):
    # 根据落子位置计算棋子中心
    center_x = 10 + 45 * x
    center_y = 10 + 45 * y

    #判断棋子颜色
    if chess == 1:
        image = Board.scaled_image_chess_black
    else:
        image = Board.scaled_image_chess_white

    #加载棋子图片
    Board.gl_screen.blit(image, (center_x, center_y))
