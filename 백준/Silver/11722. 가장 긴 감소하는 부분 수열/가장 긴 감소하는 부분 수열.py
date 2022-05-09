n = int(input())
lst = list(map(int, input().split(' ')))


def solution(n, lst):
    lst = list(reversed(lst))
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    max_dp = max(dp)
    return max_dp


print(solution(n, lst))

