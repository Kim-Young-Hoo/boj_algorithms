import sys

t = int(input())


def solution(n, turn):
    global m

    if n == 0:
        return 0

    if dp[n][turn] != -1:
        return dp[n][turn]

    dp[n][turn] = float("-inf")

    for i in range(m):
        if n - turn * lst[i] >= 0:
            dp[n][turn] = max(dp[n][turn], solution(n - turn * lst[i], turn + 1) + lst[i])
    return dp[n][turn]


for _ in range(t):

    n, m = map(int, sys.stdin.readline().split())
    lst = list(map(int, sys.stdin.readline().split()))
    lst = sorted(lst)
    dp = [[-1] * 101 for _ in range(n + 1)]
    res = solution(n, 1)

    if res != float("-inf"):
        print(res)
    else:
        print(-1)
