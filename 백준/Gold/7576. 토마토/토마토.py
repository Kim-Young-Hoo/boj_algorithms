from collections import deque

m, n = list(map(int, input().split(' ')))

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(' '))))


def sol(m, n, matrix):
    need_visit = deque([])  # queue

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                need_visit.append((i, j))

    while need_visit:

        x, y = need_visit.popleft()

        # 왼쪽
        if x > 0 and matrix[x - 1][y] == 0:
            matrix[x - 1][y] = matrix[x][y] + 1
            need_visit.append((x - 1, y))
        # 위쪽
        if y > 0 and matrix[x][y - 1] == 0:
            matrix[x][y - 1] = matrix[x][y] + 1
            need_visit.append((x, y - 1))
        # 오른쪽
        if x < n-1 and matrix[x + 1][y] == 0:
            matrix[x + 1][y] = matrix[x][y] + 1
            need_visit.append((x + 1, y))
        # 아래쪽
        if y < m-1 and matrix[x][y + 1] == 0:
            matrix[x][y + 1] = matrix[x][y] + 1
            need_visit.append((x, y + 1))


    day = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                return -1
            day = max(day, matrix[i][j])
    return day - 1


print(sol(m,n,matrix))