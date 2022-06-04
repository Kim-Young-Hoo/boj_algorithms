v, e = map(int, input().split(' '))

graph = [[float("inf")] * v for _ in range(v)]
for i in range(e):
    a, b, c = map(int, input().split(' '))
    graph[a - 1][b - 1] = c

for i in range(v):
    graph[i][i] = 0


for intermediate_node in range(len(graph)):
    new_matrix = [ele for ele in graph]

    new_matrix[intermediate_node] = graph[intermediate_node]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                new_matrix[i][j] = 0
            elif j == intermediate_node:
                new_matrix[i][j] = graph[i][j]

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i != intermediate_node and j != intermediate_node and i != j:
                new_matrix[i][j] = min(graph[i][j], graph[i][intermediate_node] + graph[intermediate_node][j])

    graph = new_matrix


min_val = float("inf")

for i in range(v):
    for j in range(v):
        if i != j:
            min_val = min(min_val, graph[i][j] + graph[j][i])
            
if min_val == float("inf"):
    print(-1)
else:
    print(min_val)