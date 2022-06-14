from collections import deque
import sys

k = int(input())


def dfs(graph, i):
    stack = deque([i])
    while stack:
        pop = stack.pop()
        if visited[pop] == 0:
            visited[pop] = 1

        for node in graph[pop]:
            if visited[node] == 0:
                if visited[pop] == 1:
                    visited[node] = 2
                    stack.append(node)
                elif visited[pop] == 2:
                    visited[node] = 1
                    stack.append(node)


def is_bipartite(visited):
    for node in graph.keys():
        for adj_node in graph[node]:
            if visited[node] == visited[adj_node]:
                return False
    return True


for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    visited = [0] * (v + 1)
    graph = {}
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, v + 1):
        if i in graph.keys() and not visited[i]:
            dfs(graph, i)
    result = is_bipartite(visited)

    if result:
        print("YES")
    else:
        print("NO")
