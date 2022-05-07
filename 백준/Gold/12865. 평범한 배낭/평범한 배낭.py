n, k = map(int, input().split(' '))

dp = [[0] * (k + 1) for _ in range(n + 1)]

w = [0]
v = [0]
for _ in range(n):
    a, b = map(int, input().split(' '))
    w.append(a)
    v.append(b)

# n = 4
# k = 8
# w = [0, 2, 3, 4, 5]
# v = [0, 1, 2, 5, 6]
# dp = [[0] * (k + 1) for _ in range(n + 1)]
# 
# w, v = zip(*sorted(zip(w, v)))


def solution(n, w, v, k):
    for r in range(1, n + 1):
        for c in range(1, k + 1):
            if c - w[r] >= 0:
                dp[r][c] = max(dp[r - 1][c], dp[r - 1][c - w[r]] + v[r])
            else:
                dp[r][c] = dp[r - 1][c]
    return dp[-1][-1]


print(solution(n, w, v, k))
