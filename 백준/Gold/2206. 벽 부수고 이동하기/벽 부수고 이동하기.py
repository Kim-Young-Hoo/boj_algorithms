import sys
from collections import deque

n, m = map(int, input().split(' '))
matrix = []

for _ in range(n):
    matrix.append(list(map(int, list(input()))))

dp = [[[float("inf")] * 2 for _ in range(m)] for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dp[0][0][0] = 0
dp[0][0][1] = 0
d = [[1, 0], [0, 1], [-1, 0], [0, -1]]

if n == 1 and m == 1:
    if matrix[0][0] == 1:
        print(-1)
    else:
        print(1)
    sys.exit()


def solution():
    global n, m

    queue = deque([(0, 0, 0, False)])

    while queue:
        x, y, dist, broke = queue.popleft()

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                if broke:
                    if matrix[nx][ny] == 1:
                        pass
                    else:
                        if not visited[nx][ny][0]:
                            dp[nx][ny][0] = min(dp[nx][ny][0], dist + 1)
                            visited[nx][ny][0] = True
                            queue.append((nx, ny, dist + 1, True))
                else:
                    if matrix[nx][ny] == 1:
                        if not visited[nx][ny][0]:
                            dp[nx][ny][0] = min(dp[nx][ny][0], dist + 1)
                            visited[nx][ny][0] = True
                            queue.append((nx, ny, dist + 1, True))

                    else:
                        if not visited[nx][ny][1]:
                            dp[nx][ny][1] = min(dp[nx][ny][1], dist + 1)
                            visited[nx][ny][1] = True
                            queue.append((nx, ny, dist + 1, False))



solution()

if min(dp[-1][-1]) != float("inf"):
    print(min(dp[-1][-1]) + 1)
else:
    print(-1)
