import pprint
import random
import sys

from collections import deque

# for _ in range(1000):

n, m = map(int, input().split(' '))
# n, m = random.choice(range(1, 5)), random.choice(range(1, 5))

walls = []
zeros = []
matrix = []
for i in range(n):
    row = list(map(int, list(input())))
    for j in range(m):
        if row[j] == 1:
            walls.append([i, j])
        else:
            zeros.append([i, j])

    matrix.append(row)

# for i in range(n):
#     row = [random.choice([0, 1])] * m
#     for j in range(m):
#         if row[j] == 1:
#             walls.append([i, j])
#         else:
#             zeros.append([i, j])
#
#     matrix.append(row)

d = [[-1, 0], [0, -1], [1, 0], [0, 1]]
group_size = {0: 0}
group_index_matrix = [[0] * m for _ in range(n)]

visited = [[0] * m for _ in range(n)]


def get_group_matrix(x, y, index):
    global n, m
    stack = deque([[x, y]])
    group_size[index] = 0

    while stack:
        x, y = stack.pop()
        group_index_matrix[x][y] = index

        if visited[x][y]:
            continue
        visited[x][y] = 1
        group_size[index] += 1

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and matrix[nx][ny] == 0:
                    stack.append([nx, ny])


def solution():
    global n, m
    for x, y in walls:
        appended_group_index_lst = []
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 0:
                    if group_index_matrix[nx][ny] not in appended_group_index_lst:
                        size = group_size[group_index_matrix[nx][ny]]
                        matrix[x][y] += size
                        matrix[x][y] %= 10
                        appended_group_index_lst.append(group_index_matrix[nx][ny])


index = 1
for i, j in zeros:
    if group_index_matrix[i][j] == 0:
        get_group_matrix(i, j, index)
        index += 1

# print(group_size)
# print(group_index_matrix)

solution()

for ele in matrix:
    print(''.join(map(str, ele)))

