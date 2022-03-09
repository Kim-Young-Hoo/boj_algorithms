import sys
sys.setrecursionlimit(10000)


t = int(input())


def sol(i, j, matrix):
    global clusters
    global count
    global already_included

    if (i, j) not in already_included:
        already_included.append((i, j))
        clusters += 1

        if i + 1 < len(matrix):
            if matrix[i + 1][j] == 1:
                sol(i + 1, j, matrix)
        if j + 1 < len(matrix[0]):
            if matrix[i][j + 1] == 1:
                sol(i, j + 1, matrix)
        if i - 1 >= 0:
            if matrix[i - 1][j] == 1:
                sol(i - 1, j, matrix)
        if j - 1 >= 0:
            if matrix[i][j - 1] == 1:
                sol(i, j - 1, matrix)
    else:
        return




for _ in range(t):

    already_included = []
    count = []

    m, n, k = list(map(int, input().split(' '))) # m = 열, n = 행
    matrix = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = list(map(int, input().split(' ')))
        matrix[x][y] = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and (i, j) not in already_included:
                clusters = 0
                sol(i, j, matrix)
                count.append(clusters)

    print(len(count))