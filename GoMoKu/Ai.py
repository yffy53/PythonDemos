import numpy as np
import random


def js_1(board, board_f):
    """p_num = 0 玩家连成子的个数
    b_num = 0 AI连成子个数
    e_num = 0 各方向空白位个数"""

    #清空评分数组
    for i in range(0, len(board_f)):
        for j in range(0, len(board_f[i])):
            board_f[i][j] = 0

    for row in range(15):
        for col in range(15):
            if row >= 0 and col >= 0 and board[row][col] == 0:  #空白点计算
                #遍历四个方向，分别计算正反方向
                d_tuple = ([1, 0], [1, 1], [0, 1], [-1, 1])
                for k in range(4):
                    x = d_tuple[k][0]
                    y = d_tuple[k][1]

                    #重置
                    p_num = 0
                    b_num = 0
                    e_num = 0

                    #对玩家正向评分
                    for i in range(1, 5):
                        if 15 > row + i * y >= 0 and 15 > col + i * x >= 0:
                            if board[row + i * y][col + i * x] == 1:
                                p_num += 1

                            #空白位
                            elif board[row + i * y][col + i * x] == 0:
                                e_num += 1
                                break
                            else:  #已有AI棋子
                                break
                        else:  #出界
                            break

                    #对玩家反向评分
                    for i in range(1, 5):
                        if 0 <= row - i * y < 15 and 0 <= col - i * x < 15:
                            if board[row - i * y][col - i * x] == 1:
                                p_num += 1

                            #空白位
                            elif board[row - i * y][col - i * x] == 0:
                                e_num += 1
                                break
                            else:  #已有AI棋子
                                break
                        else:  #出界
                            break

                    if p_num == 1:  #杀二
                        board_f[row][col] += 10
                    elif p_num == 2:
                        if e_num == 1:  #死三
                            board_f[row][col] += 30
                        elif e_num == 2:  #活三
                            board_f[row][col] += 40
                    elif p_num == 3:
                        if e_num == 1:  #死四
                            board_f[row][col] += 60
                        elif e_num == 2:  #活四
                            board_f[row][col] += 200
                    elif p_num == 4:
                        board_f[row][col] += 20000
                        #进行一次清空
                        e_num = 0

                    #对AI正向评分
                    for i in range(1, 5):
                        if 0 <= row + i * y < 15 and 0 <= col + i * x < 15:
                            if board[row + i * y][col + i * x] == 2:
                                b_num += 1
                            elif board[row + i * y][col + i * x] == 0:
                                e_num += 1
                                break
                            else:
                                break
                        else:
                            break

                    #对AI反向评分
                    for i in range(1, 5):
                        if 0 < row - i * y < 15 and 0 < col - i * x < 15:
                            if board[row - i * y][col - i * x] == 2:
                                b_num += 1
                        #空白位
                            elif board[row - i * y][col - i * x] == 0:
                                e_num += 1
                                break
                            else:
                                break
                        else:  #出界
                            break

                    if b_num == 0:  #普通下子
                        board_f[row][col] += 5
                    elif b_num == 1:  #杀二
                        board_f[row][col] += 10
                    elif b_num == 2:
                        if e_num == 1:  #死三
                            board_f[row][col] += 25
                        elif e_num == 2:  #活三
                            board_f[row][col] += 50
                    elif b_num == 3:
                        if e_num == 1:  #死四
                            board_f[row][col] += 55
                        elif e_num == 2:  #活四
                            board_f[row][col] += 300
                    elif b_num >= 4:
                        board_f[row][col] += 30000


def lz(board, board_f, x, y):
    #计算评分
    js_1(board, board_f)
    #从评分中找出最大分数
    max_score = np.max(board_f)
    #找出最大分数位置，返回到元组
    max_w = np.where(board_f == max_score)
    #最大分数个数
    num = len(max_w[0])
    list_8 = []
    k = 9999
    for i in range(num):
        if board[max_w[0][i]][max_w[1][i]] == 0:
            f = abs(max_w[0][i] - x) + abs(max_w[1][i] - y)
            if f < k:
                k = f
                list_8 = [i]
            elif f > k:
                continue
            else:
                list_8.append(i)

    num = random.choice(list_8)
    a_x = max_w[0][num]
    a_y = max_w[1][num]
    del list_8
    del max_w
    return a_x, a_y
