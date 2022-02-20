n = int(input())

lst = list(map(int, input().split(' ')))


def inc_bitonic(lst):
    dp = [0] * len(lst)
    dp[0] = 1

    for i in range(len(lst)):
        max_dp = 0
        for j in range(0, i, 1):
            if lst[j] < lst[i] and dp[j] > max_dp:
                max_dp = dp[j]
        dp[i] = max_dp + 1
    return dp


def dec_bitonic(lst):
    dp = [0] * len(lst)
    dp[-1] = 1

    for i in reversed(range(len(lst))):
        max_dp = 0
        for j in range(len(lst)-1, i-1, -1):
            if lst[j] < lst[i] and dp[j] > max_dp:
                max_dp = dp[j]
        dp[i] = max_dp + 1
    return dp


def sol(lst):

    max_bitonic = 0

    inc = inc_bitonic(lst)
    dec = dec_bitonic(lst)

    for ele1, ele2 in zip(inc, dec):
        if ele1 + ele2 > max_bitonic:
            max_bitonic = ele1 + ele2

    return max_bitonic - 1

print(sol(lst))