"""
matrix[i][j] = min(m[i, k] + m[k+1, j] + matrix[i][0] * matrix[j][1] * matrix[k][0],
                    m[i, k+1] + m[k+2, j] + matrix[i][0] * matrix[j][1] * matrix[k+1][0])
"""

n = int(input())

lst = []

for _ in range(n):
    lst.append(list(map(int, input().split(' '))))


def solution(n, lst):
    matrix = [[0] * n for _ in range(n)]

    for i in range(n-1):
        matrix[i][i+1] = lst[i][0] * lst[i+1][0] * lst[i+1][1]

    for j in range(2, n):
        for i in range(n-j):
            current_min = float("inf")
            for k in range(i, i+j):
                current_min = min(current_min, matrix[i][k] + matrix[k+1][i+j] + lst[i][0] * lst[i+j][1] * lst[k][1])
            matrix[i][i+j] = current_min
    return matrix[0][n-1]


print(solution(n, lst))