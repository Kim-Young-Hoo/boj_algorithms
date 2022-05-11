n, m = map(int, input().split(' '))
dp = [[0] * m for _ in range(n)]

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))
dp[0][0] = matrix[0][0]


def solution(n, m):
    for i in range(n):
        for j in range(m):
            if (i, j) == (0, 0):
                continue
            temp = []
            if 0 <= i - 1 < n:
                temp.append(dp[i - 1][j])
            if 0 <= j - 1 < m:
                temp.append(dp[i][j - 1])
            if 0 <= i - 1 < n and 0 <= j - 1 < m:
                temp.append(dp[i - 1][j - 1])
            dp[i][j] = max(temp) + matrix[i][j]
    return dp[n - 1][m - 1]


print(solution(n, m))
