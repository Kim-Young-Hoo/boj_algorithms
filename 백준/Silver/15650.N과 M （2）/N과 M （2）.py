n, m = list(map(int, input().split(' ')))

graph = {ele:None for ele in range(1, n+1)}
for i in graph:
    graph[i] = [ele for ele in range(i, n+1) if ele not in [i]]



def sol(start_node, n, m):
    s.append(start_node)

    if len(s) == m:
        print(' '.join(list(map(str, s))))

    for i in graph[start_node]:
        sol(i, n, m)
        s.pop()

for start in range(1, n+1):
    s = []

    sol(start, n, m)


