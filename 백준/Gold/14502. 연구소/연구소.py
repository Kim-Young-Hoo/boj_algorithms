from collections import deque

n, m = map(int, input().split(' '))
matrix = []

for _ in range(n):
    matrix.extend(list(map(int, input().split(' '))))


def solution(n, m, matrix):
    max_cnt = 0

    for i in range(len(matrix)):
        if matrix[i] != 0:
            continue
        for j in range(i+1, len(matrix)):
            if matrix[j] != 0:
                continue

            for k in range(j+1, len(matrix)):
                if matrix[k] != 0:
                    continue

                new_matrix = [0] * len(matrix)

                for x in range(len(matrix)):
                    new_matrix[x] = matrix[x]

                new_matrix[i] = 1
                new_matrix[j] = 1
                new_matrix[k] = 1

                bfs_matrix = []
                sub_list = []
                index = 0
                while new_matrix:
                    sub_list.append(new_matrix.pop(0))
                    index += 1

                    if index == m:
                        bfs_matrix.append(sub_list)
                        sub_list = []
                        index = 0


                new_matrix = bfs(n, m, bfs_matrix)

                cnt = 0
                for sub_list in new_matrix:
                    cnt += sub_list.count(0)
                max_cnt = max(max_cnt, cnt)
    return max_cnt


def bfs(n, m, matrix):
    d_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    queue = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:
                queue.append((i, j))

    while queue:

        i, j = queue.pop(0)

        for d in d_list:
            new_i = i + d[0]
            new_j = j + d[1]

            if 0 <= new_i < n and 0 <= new_j < m and matrix[new_i][new_j] == 0:
                queue.append((new_i, new_j))
                matrix[new_i][new_j] = 2

    return matrix


print(solution(n, m, matrix))