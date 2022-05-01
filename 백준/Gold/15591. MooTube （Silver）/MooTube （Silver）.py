from collections import defaultdict, deque

N, Q = map(int, input().split(' '))

graph = defaultdict(list)

for i in range(N - 1):
    p, q, r = map(int, input().split(' '))
    graph[p].append((q, r))
    graph[q].append((p, r))




def solution(graph, start_node, k):
    cnt = 0

    stack = deque([[start_node, float("inf")]])
    visited = [False] * 5001
    visited[start_node] = True
    while stack:
        pop, min_val = stack.pop()

        for node, val in graph[pop]:
            if not visited[node]:
                if min_val > val:
                    stack.append([node, val])
                    if val >= k:
                        cnt += 1
                else:
                    stack.append([node, min_val])
                    if min_val >= k:
                        cnt += 1
                visited[node] = True
    print(cnt)


for i in range(Q):
    k, v = map(int, input().split(' '))
    solution(graph, v, k)
