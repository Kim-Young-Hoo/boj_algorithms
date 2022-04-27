import random
import sys



n, k = map(int, input().split(' '))
lst = []

for _ in range(n):
    lst.append(int(input()))
# lst = [random.randrange(0, 100000) for _ in range(100)]
# k = 100000

dp = [0] * (k + 1)
dp[0] = 1


def solution(lst):

    for coin in lst:
        for i in range(1, len(dp)):
            if coin > i:
                continue
            else:
                dp[i] += dp[i-coin]

    return dp[-1]

print(solution(lst))
