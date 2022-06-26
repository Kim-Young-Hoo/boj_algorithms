import heapq
import sys

n = int(input())
m = int(input())

# graph = {ele: [] for ele in range(1, n + 1)}
graph = [[] for _ in range(n + 1)]


for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append([b, c])


a, b = map(int, input().split(' '))


def dijkstra(start_node, end_node):
    dp = [float("inf")] * (len(graph) + 1)
    dp[start_node] = 0

    heap = []
    heapq.heappush(heap, [0, start_node])
    while heap:
        val, node = heapq.heappop(heap)

        if val > dp[node]:
            continue

        for next_node, next_val in graph[node]:
            if next_val + val < dp[next_node]:
                dp[next_node] = val + next_val
                heapq.heappush(heap, (dp[next_node], next_node))
    return dp[end_node]


print(dijkstra(a, b))
