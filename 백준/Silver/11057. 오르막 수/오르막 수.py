n = int(input())

dp = [[0] * (n + 1) for _ in range(10)]

for i in range(10):
    dp[i][1] = 1


def solution(n):
    for i in range(2, n + 1):
        cum_sum = sum([ele[i - 1] for ele in dp])
        dp[0][i] = cum_sum
        for j in range(1, 10):
            cum_sum = (cum_sum - dp[j - 1][i - 1]) % 10007
            dp[j][i] = cum_sum % 10007
    return sum([ele[n] for ele in dp]) % 10007


print(solution(n))