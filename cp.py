def check_in(board, number):
    #横向检查
    for row in range(15):
        for col in range(11):
            if all(board[row][col + i] == number for i in range(5)):
                return True

    #纵向检查
    for col in range(15):
        for row in range(11):
            if all(board[row + i][col] == number for i in range(5)):
                return True

    #检查主对角线
    for row in range(11):
        for col in range(11):
            if all(board[row + i][col + i] == number for i in range(5)):
                return True

    #检查副对角线
    for row in range(11):
        for col in range(4, 15):
            if all(board[row + i][col - i] == number for i in range(5)):
                return True

    return False


def qt(board, number):
    if check_in(board, number):
        if number == 1:
            print("玩家获胜！")
        elif number == 2:
            print("AI获胜！")
        return 1
    #平局判断
    elif all(all(cell != 0 for cell in row) for row in board):
        print("平局！")
        return 2
    else:
        return 0
