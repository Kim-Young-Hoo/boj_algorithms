import random



t = int(input())


def solution(n):
    global dp

    while dp[-1] < n:
        dp.append(dp[-1] + dp[-2])

    lst = []
    idx = len(dp) - 1
    while n != 0:
        if n >= dp[idx]:
            n -= dp[idx]
            lst.append(idx)
        idx -= 1

    return ' '.join(map(str, sorted([dp[i] for i in lst if i >= 0])))


for _ in range(t):
    n = int(input())
    # n = 1000000000
    dp = [0, 1]
    print(solution(n))
