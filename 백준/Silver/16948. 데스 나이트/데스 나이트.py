from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split(' '))

matrix = [[float('inf')] * n for _ in range(n)]


def solution(n, r1, c1, r2, c2):

    # if r1 % 2 != r2 % 2:
    #     return -1
    visited = [[0] * n for _ in range(n)]

    # matrix[r1][c1] = 0
    d = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]

    queue = deque([(r1, c1, 0)])

    while queue:
        x, y, depth = queue.popleft()
        matrix[x][y] = min(matrix[x][y], depth)
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix):
                if not visited[nx][ny]:
                    queue.append((nx, ny, depth + 1))
                    visited[nx][ny] = 1
                    matrix[nx][ny] = depth + 1

    if matrix[r2][c2] == float("inf"):
        return -1

    return matrix[r2][c2]


print(solution(n, r1, c1, r2, c2))
