import sys
import heapq


V, E = map(int, input().split(' '))
k = int(input())

graph = {}
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())

    if v not in graph.keys():
        graph[v] = []

    if u not in graph.keys():
        graph[u] = [(v, w)]
    else:
        graph[u].append((v, w))


def solution(graph):
    global k
    global V

    heap = []
    dp = [float("inf")] * (V + 1)
    dp[k] = 0
    heapq.heappush(heap, (dp[k], k))

    while heap:
        current_dist, current_node = heapq.heappop(heap)

        if current_dist > dp[current_node]:
            continue

        for next_node, next_weight in graph[current_node]:
            dist = current_dist + next_weight

            if dist < dp[next_node]:
                dp[next_node] = dist
                heapq.heappush(heap, (dp[next_node], next_node))

    return dp[1:]


dp = solution(graph)

for i in range(len(dp)):
    if dp[i] == float("inf"):
        sys.stdout.write("INF" + "\n")

    else:
        sys.stdout.write(str(dp[i]) + "\n")
