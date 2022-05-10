t = int(input())


def solution(n, m):

    if m <= 1:
        return n

    for i in range(2, n+1):
        dp[i][i] = 1
        dp[i][0] = 1
        for j in range(1, i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

    return dp[n][m]

for _ in range(t):
    n, m = map(int, input().split(' '))
    dp = [[0] * (m + 2) for _ in range(m + 2)]
    dp[0][0] = 1
    dp[1][0] = 1
    dp[1][1] = 1

    print(solution(m, n))
