import sys

t = int(input())


def solution():
    global n

    current_range = 1
    while dp[0][n - 1] == float("inf"):
        current_i = 0

        while current_i + current_range < n:
            temp = []
            for div in range(current_range):
                temp.append(dp[current_i][current_i+div] + dp[current_i+div+1][current_i+current_range])
            dp[current_i][current_i + current_range] = min(temp) + sum(lst[current_i:current_i + current_range + 1])
            current_i += 1
        current_range += 1

    return dp


for _ in range(t):
    n = int(sys.stdin.readline())
    lst = list(map(int, sys.stdin.readline().split()))
    dp = [[float("inf")] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 0

    solution()
    print(dp[0][n-1])

