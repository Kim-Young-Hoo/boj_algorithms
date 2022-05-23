import sys

n, m = map(int, input().split(' '))

lst = list(map(int, input().split(' ')))

dp = [0] * n
dp[0] = lst[0]
for i in range(1, n):
    dp[i] = lst[i] + dp[i - 1]



for _ in range(m):

    i, j = map(int, sys.stdin.readline().split())
    i -= 1
    j -= 1

    if i == 0:
        print(dp[j])

    else:
        print(dp[j] - dp[i-1])
