n = int(input())

lst = list(map(int, input().split(' ')))
dp = [float("inf")] * n
dp[0] = 0

for i in range(n):
    for j in range(1, lst[i] + 1):
        if i + j < n:
            dp[i + j] = min(dp[i + j], dp[i] + 1)

if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])