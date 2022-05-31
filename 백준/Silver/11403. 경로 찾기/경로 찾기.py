n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split(' '))))


result = [ele for ele in graph]


for bridge_node in range(n):
    for current_node in range(n):
        if bridge_node == current_node:
            continue

        for destination_node in range(n):

            if graph[current_node][bridge_node]:
                if graph[bridge_node][destination_node] and not graph[current_node][destination_node]:
                    graph[current_node][destination_node] = 1

for r in result:
    print(" ".join(map(str, r)))