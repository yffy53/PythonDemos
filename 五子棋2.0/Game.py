import random
import pygame

import Board
import Player
import Login


class Game:
    def __init__(self):
        # 用户
        self.user = Login.User(Login.username_now, Login.password_now)
        #棋盘
        self.chess_board = Board.Board()
        #人玩家
        self.man = Player.Player('玩家')
        #电脑玩家
        self.computer = Player.Ai('电脑')

    # 随机先手
    def random_player(self):
        if random.randint(0, 1) == 1:
            players = [self.man, self.computer]
        else:
            players = [self.computer, self.man]
        players[0].chess = 1  #黑
        players[1].chess = -1  #白
        #print('随机到 %s 先手' % players[0].name)
        return players

    # 完整对局
    def play_round(self):
        self.chess_board.show_board()
        one_player, next_player = self.random_player()
        while True:
            one_player.move(self.chess_board)
            if self.chess_board.is_win(one_player.chess):
                self.user.num += 1
                if one_player.name == '玩家':
                    self.user.win_num += 1
                else:
                    self.user.defeat_num += 1
                Board.Board.win_draw(one_player)
                break
            if self.chess_board.is_draw():
                self.user.num += 1
                Board.Board.draw_draw()
                break
            one_player, next_player = next_player, one_player  #交换落子

    # 循环对局
    def start(self):
        while True:
            self.play_round()
            while True:
                # 等待事件发生
                event = pygame.event.wait()
                # 检查事件的类型并进行相应处理
                if event.type == pygame.QUIT:
                    # 如果事件为退出事件，则保存数据后退出程序
                    Login.write_dict_w(self.user.username, self.user.password, self.user.num, self.user.win_num, self.user.defeat_num)
                    exit('成功退出')

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 3:  #鼠标右键开始下一局
                        break
            self.chess_board.reset_board()
