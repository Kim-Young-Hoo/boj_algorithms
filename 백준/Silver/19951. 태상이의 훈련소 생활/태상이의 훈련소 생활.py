import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

cmd = [0] * (n + 1)

for _ in range(m):
    a, b, k = map(int, input().split())
    cmd[a - 1] += k
    cmd[b] -= k

dp = [0] * (n + 1)
dp[0] = cmd[0]
current_cum = cmd[0]
for i in range(1, n + 1):
    dp[i] = dp[i - 1] + cmd[i]

answer = []
for i in range(n):
    answer.append(lst[i] + dp[i])

print(*answer)