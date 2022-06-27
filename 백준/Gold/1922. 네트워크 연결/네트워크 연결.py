import sys
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
min_edge = (None, None, float("inf"))

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())

    if a == b:
        continue

    if c < min_edge[2]:
        min_edge = (a, b, c)
    graph[a].append([b, c])
    graph[b].append([a, c])


def solution(n, m, min_edge):
    cum_sum = min_edge[2]
    visited = [0] * (len(graph) + 1)
    visited[min_edge[0]] = 1
    visited[min_edge[1]] = 1
    heap = []

    for node, weight in graph[min_edge[0]]:
        if not visited[node]:
            heapq.heappush(heap, [weight, node])

    for node, weight in graph[min_edge[1]]:
        if not visited[node]:
            heapq.heappush(heap, [weight, node])

    while heap:
        weight, node = heapq.heappop(heap)
        if visited[node]:
            continue
        else:
            cum_sum += weight
            visited[node] = 1
        for next_node, next_weight in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap, [next_weight, next_node])

    return cum_sum


print(solution(n, m, min_edge))
