import pprint
from collections import deque

r, c = map(int, input().split(' '))

s = None
d = None
waters = []

matrix = []
for i in range(r):
    row = list(input())
    matrix.append(row)
    for j in range(c):
        if row[j] == "D":
            d = (i, j)
        elif row[j] == "S":
            s = (0, i, j, 0)
        elif row[j] == "*":
            waters.append((1, i, j, 0))



def solution(s, d_loc):
    global r, c
    output = "KAKTUS"


    queue = deque(waters)
    queue.append(s)

    visited = [[0] * c for _ in range(r)]

    d = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while queue:
        is_water, x, y, dist = queue.popleft()

        if not is_water:
            if x == d_loc[0] and y == d_loc[1]:
                output = dist
                return output

        for dx, dy in d:
            nx, ny = dx + x, dy + y
            if 0 <= nx < r and 0 <= ny < c:
                if is_water:
                    if matrix[nx][ny] != "D" and matrix[nx][ny] != "*" and matrix[nx][ny] != "X":
                        matrix[nx][ny] = "*"
                        queue.append((1, nx, ny, 0))
                else:
                    if not visited[nx][ny]:
                        if matrix[nx][ny] != "*" and matrix[nx][ny] != "X":
                            visited[nx][ny] = 1
                            queue.append((0, nx, ny, dist + 1))

    return output


print(solution(s, d))