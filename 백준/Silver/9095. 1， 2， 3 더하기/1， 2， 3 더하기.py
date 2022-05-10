t = int(input())


def solution(n):

    if n < 4:
        return dp[n]

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


for _ in range(t):
    n = int(input())

    dp = [0] * (n + 5)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    print(solution(n))