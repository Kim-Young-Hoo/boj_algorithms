from collections import deque

m, n = map(int, input().split(' '))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))

# m, n = 100, 100
#
# matrix = [[1] * 100 for _ in range(100)]
# matrix[0][0] = 0
# matrix[n - 1][m - 1] = 0


def sol(n, m):
    queue = deque([(0, 0)])
    dp = [[float("inf")] * m for _ in range(n)]
    dp[0][0] = 0

    d = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return dp[-1][-1]

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:

                if dp[nx][ny] > dp[x][y] + 1:
                    if matrix[nx][ny] == 1:
                        dp[nx][ny] = dp[x][y] + 1
                        queue.append((nx, ny))
                    else:
                        dp[nx][ny] = dp[x][y]
                        queue.appendleft((nx, ny))

    return dp[-1][-1]


print(sol(n, m))
