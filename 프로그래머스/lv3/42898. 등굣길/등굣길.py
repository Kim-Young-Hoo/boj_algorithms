from collections import deque


def solution(m, n, puddles):
    answer = 0

    matrix = [[0] * m for _ in range(n)]

    for puddle in puddles:
        matrix[puddle[1] - 1][puddle[0] - 1] = -1

    for i in range(m):
        if matrix[0][i] == -1:
            break
        matrix[0][i] = 1

    for i in range(n):
        if matrix[i][0] == -1:
            break
        matrix[i][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == -1:
                continue

            if matrix[i - 1][j] != -1:
                matrix[i][j] += matrix[i - 1][j] % 1000000007
            if matrix[i][j - 1] != -1:
                matrix[i][j] += matrix[i][j - 1] % 1000000007
    return matrix[-1][-1] % 1000000007
