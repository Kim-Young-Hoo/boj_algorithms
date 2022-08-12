import heapq


def solution(n, s, a, b, fares):
    answer = sol(n, s, a, b, fares)
    return answer


def sol(n, s, a, b, fares):
    graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        graph[i][i] = 0

    answer = float("inf")

    for d, e, f in fares:
        graph[d][e] = f
        graph[e][d] = f

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


    for i in range(1, n + 1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])

    return answer
