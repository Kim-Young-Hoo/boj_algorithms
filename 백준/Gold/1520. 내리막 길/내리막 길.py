import sys
sys.setrecursionlimit(5000)

m, n = list(map(int, input().split(' ')))
matrix = []

for i in range(m):
    new_line = list(map(int, input().split(' ')))
    matrix.append(new_line)

dp = [[-1] * n for _ in range(m)]


def solution(i, j):
    global m, n

    if (i, j) == (m - 1, n - 1):
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    possible = 0
    for dx, dy in d:
        if 0 <= i + dx < m and 0 <= j + dy < n and matrix[i][j] > matrix[i + dx][j + dy]:
            possible += solution(i + dx, j + dy)
    dp[i][j] = possible
    return dp[i][j]


solution(0, 0)
print(dp[0][0])
