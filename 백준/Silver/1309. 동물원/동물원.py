n = int(input())

dp = [[0] * (n+1) for _ in range(3)]
for i in range(3):
    dp[i][1] = 1


def solution(n):
    for i in range(2, n+1):
        dp[0][i] = (dp[0][i-1] % 9901 + dp[1][i-1] % 9901 + dp[2][i-1] % 9901) % 9901
        dp[1][i] = (dp[0][i-1] % 9901 + dp[2][i-1] % 9901) % 9901
        dp[2][i] = (dp[0][i-1] % 9901 + dp[1][i-1] % 9901) % 9901
    return (dp[0][n] % 9901 + dp[1][n] % 9901 + dp[2][n] % 9901) % 9901


print(solution(n))