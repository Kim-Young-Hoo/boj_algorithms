def solution(n, results):
    answer = 0

    graph = [[0] * (n + 1) for _ in range(n + 1)]

    for res in results:
        graph[res[1]][res[0]] = 1
        graph[res[0]][res[1]] = 2
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j]:
                for k in range(1, n + 1):
                    if graph[j][k] == 1 and graph[i][j] == 1:
                        graph[i][k] = 1
                    elif graph[j][k] == 2 and graph[i][j] == 2:
                        graph[i][k] = 2

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if graph[i][j]:
                for k in range(1, n + 1):
                    if graph[j][k] == 1 and graph[i][j] == 1:
                        graph[i][k] = 1
                    elif graph[j][k] == 2 and graph[i][j] == 2:
                        graph[i][k] = 2

    for sub_lst in graph:
        if len([ele for ele in sub_lst if ele != 0]) == len(graph) - 2:
            answer += 1
    return answer


solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])

[
    [0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 1, 1, 1, 1, 1],
    [0, 1, 1, 1, 1, 1],
    [0, 0, 2, 2, 0, 0],
    [0, 1, 1, 1, 1, 1]
]
