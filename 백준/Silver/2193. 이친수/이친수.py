from pprint import pprint

n = int(input())

if n == 1:
    import sys
    print(1)
    sys.exit()

dp = [[0] * (n) for _ in range(3)]
dp[1][0] = 1
dp[2][0] = 1


def solution(n):

    for i in range(1, n):
        dp[0][i] = dp[0][i - 1] + dp[1][i - 1]
        dp[1][i] = dp[0][i - 1]
        dp[2][i] = dp[0][i] + dp[1][i]
    return dp[2][n - 1]


print(solution(n))
