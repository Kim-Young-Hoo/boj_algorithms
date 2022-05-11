n, k = map(int, input().split(' '))
lst = []
for _ in range(n):
    lst.append(int(input()))
lst = list(set(lst))

dp = [float("inf")] * (k + 1)
for i in lst:
    if i < k + 1:
        dp[i] = 1


def solution():
    global k

    for i in range(k + 1):
        for coin in lst:
            if i + coin <= k:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)
    
    if dp[k] == float("inf"):
        return -1
    return dp[k]


print(solution())
