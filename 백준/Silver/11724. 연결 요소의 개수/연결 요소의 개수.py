from collections import deque

n, m = list(map(int, input().split(' ')))

graph = {}

for i in range(m):
    start, end = list(map(int, input().split(' ')))
    if start not in graph.keys():
        graph[start] = [end]
    else:
        graph[start].append(end)

    if end not in graph.keys():
        graph[end] = [start]
    else:
        graph[end].append(start)


for i in range(n-len(graph)):
    graph["solo" + str(i)] = []



def solution(graph):
    cnt = 0
    visited = []
    stack = deque([list(graph.keys())[0]])

    while stack:
        while stack:
            pop = stack.pop()
            if pop not in visited:
                visited.append(pop)

            for ele in graph[pop]:
                if ele not in visited and ele not in stack:
                    stack.append(ele)
        cnt += 1

        for ele in visited:
            del graph[ele]

        if graph.keys():
            stack.append(list(graph.keys())[0])
        visited = []

    return cnt

print(solution(graph))