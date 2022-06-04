n, m = map(int, input().split(' '))

m_lst = list(map(int, input().split(' ')))
c_lst = list(map(int, input().split(' ')))

m_lst.insert(0, 0)
c_lst.insert(0, 0)

dp = [[0] * 10001 for _ in range(n + 1)]

for i in range(1, len(dp)):
    for j in range(len(dp[0])):
        dp[i][j] = dp[i - 1][j]
        if j - c_lst[i] >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - c_lst[i]] + m_lst[i])

min_res = float("inf")

for i in range(1, len(dp)):
    for j in range(len(dp[0])):
        if dp[i][j] >= m:
            min_res = min(min_res, j)

print(min_res)