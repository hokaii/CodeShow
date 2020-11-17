import random
import pygame
pygame.init()

game_state = 0 # 游戏状态 1. 表示正常进行, 2. 表示X胜 3. 表示O胜 4. 表示平局
# 设定获胜的组合方式(横、竖、斜)
WINNING_TRIADS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6))
# 用一维列表表示棋盘:
SLOTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)
# -1表示X玩家 0表示空位 1表示O玩家.
X_token = -1
Open_token = 0
O_token = 1
END_PHRASE = ('平局', '胜利', '失败')
location_dict = {0: [1, 1], 1: [3, 1], 2: [5, 1], 3: [1, 3], 4: [3, 3], 5: [5, 3], 6: [1, 5], 7: [3, 5], 8: [5, 5]}

def alpha_beta_valuation(board, player, next_player, alpha, beta):
    """运用AlphaBeta剪枝来计算当前局面的分值
       因为搜索层数少，总能搜索到最终局面，估值结果为[-1,0,1]
    """
    wnnr = winner(board)
    if wnnr != Open_token:
        # 有玩家获胜
        return wnnr
    elif not legal_move_left(board):
        # 没有空位,平局
        return 0
    # 检查当前玩家"player"的所有可落子点
    for move in SLOTS:
        if board[move] == Open_token:
            board[move] = player
            # 落子之后交换玩家，继续检验
            val = alpha_beta_valuation(board, next_player, player, alpha, beta)
            board[move] = Open_token
            if player == O_token:  # 当前玩家是O,是Max玩家(记号是1)
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta  # 直接返回当前的最大可能取值beta, 进行剪枝
            else:  # 当前玩家是X,是Min玩家(记号是-1)
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha  # 直接返回当前的最小可能取值alpha, 进行剪枝
    if player == O_token:
        retval = alpha
    else:
        retval = beta
    return retval

def legal_move_left(board):
    """ 判断棋盘上是否还有空位 """
    for slot in SLOTS:
        if board[slot] == Open_token:
            return True
    return False

def winner(board):
    """ 判断局面的胜者,返回值-1表示X获胜,1表示O获胜,0表示平局或者未结束"""
    for triad in WINNING_TRIADS:
        triad_sum = board[triad[0]] + board[triad[1]] + board[triad[2]]
        if triad_sum == 3:
            game_state = 3
            return board[triad[0]]  # 表示棋子的数值恰好也是-1:X,1:O
        if triad_sum == -3:
            game_state = 2
            return board[triad[0]]
    return 0

def determine_move(board):
    # 决定电脑(玩家O)的下一步棋,若估值相同则随机选取步数
    best_val = -2  # 估值结果只在[-1,0,1]中
    my_moves = []
    for move in SLOTS:
        if board[move] == Open_token:
            board[move] = O_token
            val = alpha_beta_valuation(board, X_token, O_token, -2, 2)
            board[move] = Open_token
            print("Computer如果下在", move, ",将导致", END_PHRASE[val])
            if val > best_val:
                best_val = val
                my_moves = [move]
            if val == best_val:
                my_moves.append(move)
    return random.choice(my_moves)

def print_board(board):
    """打印当前棋盘"""
    chess_color = (255, 255, 255)
    for i in range(9):
        status = board[i]
        x = location_dict[i][0]
        y = location_dict[i][1]
        if status == -1:
            pygame.draw.circle(screen, chess_color, [(cell_size//2)*x + space, (cell_size//2)*y + space], 30, 30)
        elif status == 1:
            x = (x - 1) /2
            y = (y-1) /2
            pygame.draw.aaline(screen, chess_color, (x * cell_size, y * cell_size), ((x+1) * cell_size, (y+1)*cell_size), 1)
            pygame.draw.aaline(screen, chess_color, ((x+1) * cell_size, y * cell_size), (x * cell_size, (y+1)*cell_size), 1)

HUMAN = 1
COMPUTER = 0
next_move = HUMAN
opt = input("请选择先手方，输入X表示玩家先手，输入O表示电脑先手：")
if opt == "X":
    next_move = HUMAN
elif opt == "O":
    next_move = COMPUTER
else:
    print("输入有误，默认玩家先手")
board = [Open_token for i in range(9)]
space = 1 # 边距
cell_size = 70 # 格子大小
cell_num = 4
grid_size = cell_size * (cell_num - 1) + space * 2# 棋盘大小
screen_caption = pygame.display.set_caption('井字棋')
screen = pygame.display.set_mode((grid_size, grid_size)) # 设置窗口长宽
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if legal_move_left(board) and winner(board) == Open_token and event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = int((x - space) * 1.0 / cell_size)
            yi = int((y - space) * 1.0 / cell_size)
            xi = xi * 2 + 1
            yi = yi * 2 + 1
            but = 0
            if xi == 1:
                if yi == 1:
                    but = 0
                elif yi == 3:
                    but = 3
                else:
                    but = 6
            elif xi == 3:
                if yi == 1:
                    but = 1
                elif yi == 3:
                    but = 4
                else:
                    but = 7
            else:
                if yi == 1:
                    but = 2
                elif yi == 3:
                    but = 5
                else:
                    but = 8
            if next_move == HUMAN and legal_move_left(board):
                try:
                    humanmv = but
                    if board[humanmv] != Open_token:
                        continue
                    board[humanmv] = X_token
                    next_move = COMPUTER
                except:
                    print("输入有误，请重试")
                    continue
            if next_move == COMPUTER and legal_move_left(board):
                mymv = determine_move(board)
                print("Computer最终决定下在", mymv)
                board[mymv] = O_token
                next_move = HUMAN
    screen.fill((0, 0, 0)) # 将界面设置为黑色
    for x in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x + space, 0 + space), (x + space, cell_size*(cell_num-1)+space), 1)
    for y in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0 + space, y + space), (cell_size*(cell_num-1)+space, y+space), 1)
    chess_color = (255, 255, 255)
    for i in range(9):
        status = board[i]
        x = location_dict[i][0]
        y = location_dict[i][1]
        if status == -1:
            pygame.draw.circle(screen, chess_color, [(cell_size // 2) * x + space, (cell_size // 2) * y + space], 30,
                               30)
        elif status == 1:
            x = (x - 1) / 2
            y = (y - 1) / 2
            pygame.draw.aaline(screen, chess_color, (x * cell_size, y * cell_size),
                               ((x + 1) * cell_size, (y + 1) * cell_size), 1)
            pygame.draw.aaline(screen, chess_color, ((x + 1) * cell_size, y * cell_size),
                               (x * cell_size, (y + 1) * cell_size), 1)
    if game_state == 0:
        game_state = winner(board)
        if game_state != Open_token:
            if game_state == -1:
                game_state = 2
            else:
                game_state = 3
        elif 0 not in board:
            game_state = 4
    else:
        myfont = pygame.font.Font(None, 40)
        color = 255, 255, 255
        win_text = "%s win" % ('you' if game_state == 2 else 'computer')
        if game_state == 4:
            win_text = "dogfall!"
        textImage = myfont.render(win_text, True, color)
        screen.fill((0, 0, 0))
        if game_state == 4:
            location = (50, 90)
        else:
            location = (10, 90)
        screen.blit(textImage, location)
        pygame.display.flip()
    pygame.display.update()

"""
import random

# 用如下的9个数字来表示棋盘的位置:
# 0  1  2
# 3  4  5
# 6  7  8

# 设定获胜的组合方式(横、竖、斜)
WINNING_TRIADS = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6))
# 设定棋盘按一行三个打印
PRINTING_TRIADS = ((0, 1, 2), (3, 4, 5), (6, 7, 8))
# 用一维列表表示棋盘:
SLOTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)
# -1表示X玩家 0表示空位 1表示O玩家.
X_token = -1
Open_token = 0
O_token = 1

MARKERS = ['_', 'O', 'X']
END_PHRASE = ('平局', '胜利', '失败')

HUMAN = 1
COMPUTER = 0

def alpha_beta_valuation(board, player, next_player, alpha, beta):
    # board, X_token, O_token, -2, 2
    #运用alpha,beta剪枝计算当前局面的分值
    #因为搜索层面少, 总能搜索到最终局面, 估值结果为[-1,0,1]
    wnnr = winner(board)
    if wnnr != Open_token:
        # 有玩家获胜
        return wnnr
    elif not legal_move_left(board):
        # 没有空位
        return 0
    # 检查当前玩家"player"的所有可落子点
    # 棋盘SLOTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    # Open_token = 0表示空位 X_token = -1表示X玩家 O_token = 1表示电脑
    for move in SLOTS:
        if board[move] == Open_token:
            board[move] = player
            # 落子后交换玩家, 继续校验
            val = alpha_beta_valuation(board, next_player, player, alpha, beta)
            board[move] = Open_token
            if player == O_token:# 当前玩家是0, 是Max玩家(记号是1)
                if val > alpha:
                    alpha = val
                if alpha >= beta:
                    return beta# 触发剪枝, 直接返回当前的最大可能取值beta
            else:# 当前玩家是X, 是Min玩家(记号是-1)
                if val < beta:
                    beta = val
                if beta <= alpha:
                    return alpha# 触发剪枝, 直接返回当前的最小可能取值alpha
    if player == O_token:
        ret_val = alpha
    else:
        ret_val = beta
    return ret_val


def legal_move_left(board):
    #判断棋盘上是否还有空位
    for slot in SLOTS:
        if board[slot] == Open_token:
            return True
    return False

def winner(board):
    #判断局面的胜者, 返回-1表示X获胜, 1表示0获胜, 0表示平局或者未结束
    for triad in WINNING_TRIADS:
        triad_sum = board[triad[0]] + board[triad[1]] + board[triad[2]]
        if triad_sum == 3 or triad_sum == -3:
            return board[triad[0]]# 表示棋子的数值恰好也是-1: X获胜, 1: 0获胜
    return 0

def print_board(board):
    #打印棋盘
    for row in PRINTING_TRIADS:
        r = ' '
        for hole in row:
            r += MARKERS[board[hole]] + ' '
        print(r)

def determine_move(board):
    #决定电脑(玩家0)的下一步棋, 若估值相同则随机选取步数
    best_val = -2 # 估值结果只在[-1, 0, 1]中
    my_moves = []
    print("开始思考")
    # 棋盘SLOTS = (0, 1, 2, 3, 4, 5, 6, 7, 8)
    # Open_token = 0表示空位 X_token = -1表示X玩家 O_token = 1表示电脑
    for move in SLOTS:
        if board[move] == Open_token:
            board[move] = O_token
            val = alpha_beta_valuation(board, X_token, O_token, -2, 2)
            board[move] = Open_token
            print("Computer如果下在", move, ", 将导致", END_PHRASE[val])
            if val > best_val:
                best_val = val
                my_moves = [move]
            if val == best_val:
                my_moves.append(move)
    return random.choice(my_moves)




def main():
    #决定谁是X(先手)
    next_move = HUMAN
    opt = input("请输入先手方, 输入X表示玩家先手, 输入0表示电脑先手: ")
    if opt == "X":
        next_move = HUMAN
    elif opt == "O":
        next_move = COMPUTER
    else:
        print("输入有误, 默认玩家先手")

    # 初始化空棋盘, 初始都为0
    board = [Open_token for i in range(9)]

    # 开始下棋, 先判断棋盘上还有空位 且 没有一方获胜或平局
    while legal_move_left(board) and winner(board) == Open_token:
        print()
        print_board(board)
        if next_move == HUMAN and legal_move_left(board):
            try:
                human_mv = int(input("请输入你要落子的位置(0-8): "))
                if board[human_mv] != Open_token:# 下在有棋子的地方
                    continue
                board[human_mv] = X_token
                next_move = COMPUTER
            except:
                print("输入有误, 请重试")
                continue
        if next_move == COMPUTER and legal_move_left(board):
            my_mv = determine_move(board)
            print("Computer最终决定下在", my_mv)
            board[my_mv] = O_token
            next_move = HUMAN

    # 输出结果
    print_board(board)
    print(["平局", "Computer赢了", "你赢你"][winner(board)])


if __name__ == '__main__':
    main()


import random
import pygame
pygame.init()

space = 1 # 边距
cell_size = 70 # 格子大小
cell_num = 4
grid_size = cell_size * (cell_num - 1) + space * 2# 棋盘大小
screen_caption = pygame.display.set_caption('井字棋')
screen = pygame.display.set_mode((grid_size, grid_size)) # 设置窗口长宽

chess_arr = []
flag = 1 # 1X, 2O
game_state = 1 # 游戏状态1. 表示正常进行, 2. 表示X胜 3. 表示O胜

def check_win(chess_arr, flag):
    return False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_state == 1 and event.type == pygame.MOUSEBUTTONUP:
            x, y = pygame.mouse.get_pos()
            xi = int((x-space) * 1.0 / cell_size)
            yi = int((y - space) * 1.0 / cell_size)
            xi = xi * 2 + 1
            yi = yi * 2 + 1
            print(x, y)
            print(xi, yi)
            if (xi, yi, 1) not in chess_arr and (xi, yi, 2) not in chess_arr:
                chess_arr.append((xi, yi, flag))
                if check_win(chess_arr, flag):
                    game_state = 2 if flag == 1 else 3
                else:
                    flag = 2 if flag == 1 else 1

    screen.fill((0, 0, 0)) # 将界面设置为黑色

    for x in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x + space, 0 + space), (x + space, cell_size*(cell_num-1)+space), 1)
    for y in range(0, cell_size * cell_num, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0 + space, y + space), (cell_size*(cell_num-1)+space, y+space), 1)

    for x, y, c in chess_arr:
        chess_color = (255, 255, 255)
        if c != 1:
            pygame.draw.circle(screen, chess_color, [(cell_size//2)*x + space, (cell_size//2)*y + space], 30, 30)
        else:
            x = (x - 1) /2
            y = (y-1) /2
            pygame.draw.aaline(screen, chess_color, (x * cell_size, y * cell_size), ((x+1) * cell_size, (y+1)*cell_size), 1)
            pygame.draw.aaline(screen, chess_color, ((x+1) * cell_size, y * cell_size), (x * cell_size, (y+1)*cell_size), 1)

    if game_state != 1:
        myfont = pygame.font.Font(None, 60)
        white = 210, 210, 0
        win_text = "%s win" % ('black' if game_state == 2 else 'white')
        textImage = myfont.render(win_text, True, white)
        screen.blit(textImage, (260, 320))
    pygame.display.update()
"""