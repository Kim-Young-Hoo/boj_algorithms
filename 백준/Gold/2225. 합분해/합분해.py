n, k = map(int, input().split(' '))
dp = [[0] * (n + 1) for _ in range(k + 1)]

for i in range(len(dp)):
    dp[i][0] = 1
dp[0][0] = 0


def solution(n, k):
    for i in range(1, k + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] % 1000000000 + dp[i][j - 1] % 1000000000) % 1000000000

    return dp[-1][-1]


print(solution(n, k))

