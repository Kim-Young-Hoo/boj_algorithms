n, m = list(map(int, input().split(' ')))
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input())))

dp = [[float("inf")] * m for _ in range(n)]
dp[0][0] = 0


def sol(n, m, matrix):
    already_visit = []
    need_visit = [(0, 0)]  # queue - bfs로 돌아야됨

    while need_visit:
        x, y = need_visit.pop(0)
        if (x, y) in already_visit:
            continue
        else:
            already_visit.append((x, y))

        left_dp = float("inf")
        right_dp = float("inf")
        up_dp = float("inf")
        down_dp = float("inf")
        if x - 1 >= 0:
            left_dp = dp[x - 1][y]
        if y - 1 >= 0:
            up_dp = dp[x][y - 1]
        if x + 1 < n:
            right_dp = dp[x + 1][y]
        if y + 1 < m:
            down_dp = dp[x][y + 1]

        dp[x][y] = min(dp[x][y], left_dp, right_dp, up_dp, down_dp) + 1

        if x - 1 >= 0:
            if matrix[x - 1][y] == 1:
                need_visit.append((x - 1, y))

        if y - 1 >= 0:
            if matrix[x][y - 1] == 1:
                need_visit.append((x, y - 1))

        if x + 1 < n:
            if matrix[x + 1][y] == 1:
                need_visit.append((x + 1, y))

        if y + 1 < m:
            if matrix[x][y + 1] == 1:
                need_visit.append((x, y + 1))


sol(n, m, matrix)
print(dp[n - 1][m - 1])
