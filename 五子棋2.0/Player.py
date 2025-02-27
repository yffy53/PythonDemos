import pygame
import random
import numpy as np


class Player:
    def __init__(self, name):
        #姓名
        self.name = name
        #棋子
        self.chess = None
        #可悔棋次数
        self.back_num = 3

    def move(self, chess_board):  #落子
        while True:
            # 等待事件发生
            event = pygame.event.wait()
            # 检查事件的类型并进行相应处理
            if event.type == pygame.QUIT:
                # 如果事件为退出事件，则退出程序
                exit('成功退出')

            if event.type == pygame.MOUSEBUTTONDOWN:
                #判断鼠标事件，1左键，3右键
                if event.button == 1:
                    #print('鼠标按下', event.pos)
                    # 获取鼠标点击位置
                    mouse_x, mouse_y = event.pos
                    # 计算落子位置
                    p_x = (mouse_x - 13) // 45
                    p_y = (mouse_y - 13) // 45
                    if chess_board.move_down(p_x, p_y, self.chess, self.name):
                        return
                elif event.button == 3 and self.back_num > 0:  #可悔棋次数大于0
                    self.back_num -= 1
                    chess_board.move_back()


class Ai(Player):
    def __init__(self, name):
        super().__init__(name)

        # 分数棋盘
        self.board_score = np.zeros((15, 15), dtype=int)

    #计算棋局分数
    def score_board(self, chess_board):
        # 清空评分数组
        for i in range(0, len(self.board_score)):
            for j in range(0, len(self.board_score[i])):
                self.board_score[i][j] = 0

        for row in range(15):
            for col in range(15):
                if row >= 0 and col >= 0 and chess_board[row][col] == 0:  # 空白点计算
                    # 遍历四个方向，分别计算正反方向
                    d_tuple = ([1, 0], [1, 1], [0, 1], [-1, 1])
                    for k in range(4):
                        x = d_tuple[k][0]
                        y = d_tuple[k][1]

                        # 重置
                        p_num = 0
                        b_num = 0
                        e_num = 0

                        # 对玩家正向评分
                        for i in range(1, 5):
                            if 15 > row + i * y >= 0 and 15 > col + i * x >= 0:
                                if chess_board[row + i * y][col + i * x] == self.chess * (-1):
                                    p_num += 1

                                # 空白位
                                elif chess_board[row + i * y][col + i * x] == 0:
                                    e_num += 1
                                    break
                                else:  # 已有AI棋子
                                    break
                            else:  # 出界
                                break

                        # 对玩家反向评分
                        for i in range(1, 5):
                            if 0 <= row - i * y < 15 and 0 <= col - i * x < 15:
                                if chess_board[row - i * y][col - i * x] == self.chess * (-1):
                                    p_num += 1

                                # 空白位
                                elif chess_board[row - i * y][col - i * x] == 0:
                                    e_num += 1
                                    break
                                else:  # 已有AI棋子
                                    break
                            else:  # 出界
                                break

                        if p_num == 1:  # 杀二
                            self.board_score[row][col] += 10
                        elif p_num == 2:
                            if e_num == 1:  # 死三
                                self.board_score[row][col] += 30
                            elif e_num == 2:  # 活三
                                self.board_score[row][col] += 40
                        elif p_num == 3:
                            if e_num == 1:  # 死四
                                self.board_score[row][col] += 60
                            elif e_num == 2:  # 活四
                                self.board_score[row][col] += 200
                        elif p_num == 4:
                            self.board_score[row][col] += 20000
                            # 进行一次清空
                            e_num = 0

                        # 对AI正向评分
                        for i in range(1, 5):
                            if 0 <= row + i * y < 15 and 0 <= col + i * x < 15:
                                if chess_board[row + i * y][col + i * x] == self.chess:
                                    b_num += 1
                                elif chess_board[row + i * y][col + i * x] == 0:
                                    e_num += 1
                                    break
                                else:
                                    break
                            else:
                                break

                        # 对AI反向评分
                        for i in range(1, 5):
                            if 0 < row - i * y < 15 and 0 < col - i * x < 15:
                                if chess_board[row - i * y][col - i * x] == self.chess:
                                    b_num += 1
                                # 空白位
                                elif chess_board[row - i * y][col - i * x] == 0:
                                    e_num += 1
                                    break
                                else:
                                    break
                            else:  # 出界
                                break

                        if b_num == 0:  # 普通下子
                            self.board_score[row][col] += 5
                        elif b_num == 1:  # 杀二
                            self.board_score[row][col] += 10
                        elif b_num == 2:
                            if e_num == 1:  # 死三
                                self.board_score[row][col] += 25
                            elif e_num == 2:  # 活三
                                self.board_score[row][col] += 50
                        elif b_num == 3:
                            if e_num == 1:  # 死四
                                self.board_score[row][col] += 55
                            elif e_num == 2:  # 活四
                                self.board_score[row][col] += 300
                        elif b_num >= 4:
                            self.board_score[row][col] += 30000

    #电脑先手落子
    def move_one(self, chess_board):
        # 落子天元
        chess_board.move_down(7, 7, self.chess)

    #电脑后手落子
    def move_tow(self, chess_board):
        # 计算评分
        self.score_board(chess_board)
        # 从评分中找出最大分数
        return np.max(self.board_score)

    def move(self, chess_board):
        # 从评分中找出最大分数
        max_score = self.move_tow(chess_board)
        # 找出最大分数位置，返回到元组
        max_position = np.where(self.board_score == max_score)
        # 最大分数个数
        max_score_num = len(max_position[0])
        if max_score_num == 15 * 15:  #棋盘各位置分数相同
            self.move_one(chess_board)
        else:
            max_position_col = random.randint(0,  max_score_num-1)  #从最大分数中随机落子
            row = max_position[0][max_position_col]
            col = max_position[1][max_position_col]
            # 落子
            chess_board.move_down(row, col, self.chess)
