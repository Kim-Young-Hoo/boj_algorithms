import sys
from pprint import pprint

r, c = map(int, input().split(' '))
matrix = []
for _ in range(r):
    matrix.append(list(sys.stdin.readline().rstrip()))

d = [[-1, 1], [0, 1], [1, 1]]


def solution(x, y):
    global r, c
    if y == c - 1:
        matrix[x][y] = "x"
        return "x"

    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < r and 0 <= ny < c and matrix[nx][ny] == ".":
            res = solution(nx, ny)
            matrix[x][y] = res

            if res == "x":
                return matrix[x][y]

    return "-"


for i in range(r):
    solution(i, 0)

cnt = 0
for i in range(r):
    if matrix[i][c - 1] == "x":
        cnt += 1

print(cnt)
# pprint(matrix)