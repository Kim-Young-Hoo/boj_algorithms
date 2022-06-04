c, n = map(int, input().split(' '))

lst = [[0, 0]]
for _ in range(n):
    temp = list(map(int, input().split(' ')))
    lst.append(temp)

dp = [[0] * 100001 for _ in range(n + 1)]

for i in range(1, len(lst)):
    for j in range(len(dp[0])):
        dp[i][j] = dp[i - 1][j]
        if j - lst[i][0] >= 0:
            temp = [lst[i][1] + dp[i - 1][j - lst[i][0]], lst[i][1] + dp[i][j - lst[i][0]]]
            dp[i][j] = max(dp[i][j], max(temp))

min_val = float("inf")

for i in range(1, len(lst)):
    for j in range(len(dp[0])):
        if dp[i][j] >= c:
            min_val = min(min_val, j)

print(min_val)
