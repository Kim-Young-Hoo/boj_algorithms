n = int(input())

count = 0


def board_maker(board, start):
    board[start[0]][start[1]] = False

    # x좌표 왼쪽
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if x == 0:
            break
        x -= 1
        board[x][y] = False

    # y좌표 위쪽
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if y == 0:
            break
        y -= 1
        board[x][y] = False

    # x 오른쪽
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if x == len(board) - 1:
            break
        x += 1
        board[x][y] = False

    # y 아래쪽
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if y == len(board) - 1:
            break
        y += 1
        board[x][y] = False


    # 대각 왼위
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if x == 0 or y == 0:
            break
        x -= 1
        y -= 1
        board[x][y] = False

    # 대각 오위
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if x == len(board) - 1 or y == 0:
            break
        x += 1
        y -= 1
        board[x][y] = False

    # 대각 왼아래
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if x == 0 or y == len(board) - 1:
            break
        x -= 1
        y += 1
        board[x][y] = False

    # 대각 오아래
    x, y = [start[0], start[1]]
    for i in range(len(board)):
        if x == len(board) - 1 or y == len(board) - 1:
            break
        x += 1
        y += 1
        board[x][y] = False
    return board


def sol(board, start, n_queen):
    global count

    if n_queen == len(board):
        count += 1
        return

    new_board = board_maker(board, start)

    for i in range(len(board)):
        for j in range(len(board)):
            if new_board[i][j]:
                sol(new_board, [i, j], n_queen + 1)



for i in range(n):
    for j in range(n):
        board = [[True] * n for _ in range(n)]
        sol(board, [i, j], 1)

# sol(board, [0,1], 1)


print(count / n)