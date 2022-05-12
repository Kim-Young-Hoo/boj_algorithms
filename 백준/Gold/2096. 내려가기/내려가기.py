import sys

n = int(input())

max_dp = []
min_dp = []

for _ in range(n):
    max_temp = [0, 0, 0]
    min_temp = [0, 0, 0]
    lst = list(map(int, sys.stdin.readline().split()))

    if not max_dp:
        max_dp = lst
        min_dp = lst
        continue

    max_temp[0] = max(lst[0] + max_dp[0], lst[0] + max_dp[1])
    max_temp[1] = max(lst[1] + max_dp[0], lst[1] + max_dp[1], lst[1] + max_dp[2])
    max_temp[2] = max(lst[2] + max_dp[2], lst[2] + max_dp[1])
    max_dp = [ele for ele in max_temp]

    min_temp[0] = min(lst[0] + min_dp[0], lst[0] + min_dp[1])
    min_temp[1] = min(lst[1] + min_dp[0], lst[1] + min_dp[1], lst[1] + min_dp[2])
    min_temp[2] = min(lst[2] + min_dp[2], lst[2] + min_dp[1])
    min_dp = [ele for ele in min_temp]


print(max(max_dp), min(min_dp))