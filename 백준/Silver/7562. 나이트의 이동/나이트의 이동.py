def solution(l, start, end):

    if start == end:
        return 0

    direction = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [1, -2], [2, -1], [2, 1], [1, 2]]
    board = [[0] * l for _ in range(l)]
    queue = [start]

    while queue:
        pop = queue.pop(0)
        x, y = pop

        for d in direction:
            dx, dy = [x + d[0], y + d[1]]

            if 0 <= dx < l and 0 <= dy < l:
                if dx == end[0] and dy == end[1]:
                    return board[x][y] + 1

                if board[dx][dy] == 0:
                    board[dx][dy] = board[x][y] + 1
                    queue.append([dx, dy])

    return board


n = int(input())

for i in range(n):
    l = int(input())
    start = list(map(int, input().split(' ')))
    end = list(map(int, input().split(' ')))
    print(solution(l, start, end))
