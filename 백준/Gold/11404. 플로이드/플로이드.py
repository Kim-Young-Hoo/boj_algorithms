import sys

n = int(input())
m = int(input())

matrix = [[float("inf")] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    matrix[i][i] = 0
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if matrix[a][b] > c:
        matrix[a][b] = c


def floyd_warshall(n):
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(1, n + 1):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix[i][j] == float("inf"):
                matrix[i][j] = 0

    for i in range(1, n + 1):
        print(*matrix[i][1:])


floyd_warshall(n)

# [
#     [0, inf, inf, inf, inf, inf],
#     [inf, 0, 2, 3, 2, 5],
#     [inf, 12, 0, 15, 2, 5],
#     [inf, 8, 9, 0, 2, 5],
#     [inf, 10, 7, 13, 0, 3],
#     [inf, 7, 4, 10, 6, 0]
# ]
