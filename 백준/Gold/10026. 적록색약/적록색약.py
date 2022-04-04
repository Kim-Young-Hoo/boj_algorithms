from collections import deque

n = int(input())

matrix = []

for i in range(n):
    matrix.append(list(map(str, list(input()))))


def solution(n, matrix):
    d_list = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    normal_cnt = 0
    rg_cnt = 0

    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([[0, 0]])

    for i in range(n):
        for j in range(n):

            if visited[i][j] == 0:

                queue.append([i, j])

                while queue:

                    pop = queue.pop()
                    visited[pop[0]][pop[1]] = 1

                    for dx, dy in d_list:
                        new_x = pop[0] + dx
                        new_y = pop[1] + dy

                        if 0 <= new_x < n and 0 <= new_y < n and [new_x, new_y] and visited[new_x][new_y] == 0:

                            if matrix[pop[0]][pop[1]] == matrix[new_x][new_y]:
                                queue.append([new_x, new_y])

                normal_cnt += 1


    matrix = [['R' if c == 'G' else c for c in row] for row in matrix]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    queue = deque([[0, 0]])

    for i in range(n):
        for j in range(n):

            if visited[i][j] == 0:

                queue.append([i, j])

                while queue:

                    pop = queue.pop()
                    visited[pop[0]][pop[1]] = 1

                    for dx, dy in d_list:
                        new_x = pop[0] + dx
                        new_y = pop[1] + dy

                        if 0 <= new_x < n and 0 <= new_y < n and [new_x, new_y] and visited[new_x][new_y] == 0:

                            if matrix[pop[0]][pop[1]] == matrix[new_x][new_y]:
                                queue.append([new_x, new_y])

                rg_cnt += 1

    return ' '.join([str(normal_cnt), str(rg_cnt)])


print(solution(n, matrix))