from collections import deque

n, m = map(int, input().split(' '))
# matrix = [[0] * (n + 1) for _ in range(n + 1)]

graph = {i: {} for i in range(1, n + 1)}
max_val = 0

for _ in range(m):
    a, b, c = map(int, input().split(' '))
    if b in graph[a].keys():
        graph[a][b] = max(graph[a][b], c)
    else:
        graph[a][b] = c

    if a in graph[b].keys():
        graph[b][a] = max(graph[b][a], c)
    else:
        graph[b][a] = c
    max_val = max(max_val, c)

f1, f2 = map(int, input().split(' '))

start = 0
end = max_val


def check(f1, f2, mid):
    global n
    queue = deque([f1])
    visited = [0] * (n + 1)

    possible = False
    while queue:
        pop = queue.popleft()
        if pop == f2:
            possible = True
            break

        for key, val in graph[pop].items():
            if not visited[key] and val >= mid:
                visited[key] = 1
                queue.append(key)

    return possible


while start <= end:
    mid = (start + end) // 2
    if check(f1, f2, mid):
        start = mid + 1
    else:
        end = mid - 1

print(end)
