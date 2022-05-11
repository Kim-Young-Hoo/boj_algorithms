n = int(input())
lst = list(map(int, input().split(' ')))

dp = [ele for ele in lst]


def solution(n):
    for i in range(n):
        for j in range(0, i):
            if lst[j] < lst[i]:
                dp[i] = max(dp[i], dp[j] + lst[i])

    return max(dp)


print(solution(n))
