import sys

n, m = map(int, input().split(' '))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, sys.stdin.readline().split())))

cum_sum = [[0] * (n + 1) for _ in range(n + 1)]
cum_sum[1][1] = matrix[0][0]
for i in range(1, n):
    cum_sum[1][i] = cum_sum[1][i - 1] + matrix[1][i]
    cum_sum[i][1] = cum_sum[i - 1][1] + matrix[i][1]

for i in range(n):
    for j in range(n):
        cum_sum[i][j] = cum_sum[i][j - 1] + cum_sum[i - 1][j] - cum_sum[i - 1][j - 1] + matrix[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1

    print(cum_sum[x2][y2] - cum_sum[x1 - 1][y2] - cum_sum[x2][y1 - 1] + cum_sum[x1 - 1][y1 - 1])
