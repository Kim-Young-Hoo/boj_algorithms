n = int(input())
lst = list(map(int, input().split(' ')))


def sol(lst):
    dp = [0] * len(lst)
    dp[0] = lst[0]

    for i in range(1, len(lst)):
        dp[i] = max(dp[i-1] + lst[i], lst[i])


    return max(dp)


print(sol(lst))
