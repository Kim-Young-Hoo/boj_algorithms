"""
https://ko.wikipedia.org/wiki/%EC%9D%B4%ED%95%AD_%EA%B3%84%EC%88%98

n! / (k!(n-k)!)    0<=k<=n
0                   k<0
0                   k>n

"""
n, k = map(int, input().split(' '))

dp = [[-1] * (k + 1) for _ in range(n + 1)]


def solution(n, k):
    if k < 0 or k > n:
        return 0

    if k == 0:
        return 1

    if k == 1:
        return n

    if dp[n][k] > -1:
        return dp[n][k]

    dp[n][k] = ((solution(n - 1, k - 1) % 10007) + (solution(n - 1, k) % 10007)) % 10007

    return dp[n][k]


print(solution(n, k))
