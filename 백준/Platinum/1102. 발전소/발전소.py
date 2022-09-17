import sys;input = sys.stdin.readline

N = int(input().strip())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
mask = input().strip()
mask = mask[::-1]

bit, count = 0, 0
for m in mask:
    bit <<= 1
    if m == 'Y':
        bit |= 1
        count += 1
P = int(input().strip())
dp = [float('inf')] * (1 << N)


def DFS(mask, cnt):
    global dp

    if cnt >= P:
        return 0

    if dp[mask] != float('inf'):
        return dp[mask]

    for i in range(N):
        if mask & (1 << i):
            for j in range(N):
                if mask & (1 << j) == 0:
                    dp[mask] = min(dp[mask], graph[i][j] + DFS(mask | 1 << j, cnt + 1))

    return dp[mask]


ans = DFS(bit, count)
print(-1 if ans == float('inf') else ans)
