n, m = map(int, input().split(' '))

graph = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(len(graph)):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a][b] = 1


def solution(n):
    # for _ in range(n + 1):
    for k in range(n + 1):
        for i in range(n + 1):
            for j in range(n + 1):
                if not graph[i][j] and graph[j][i] == 1:
                    graph[i][j] = 2

                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

                if graph[j][k] == 1 and graph[k][i] == 1:
                    graph[i][j] = 2

    cnt = 0
    for row in graph:
        if row.count(0) == 2:
            cnt += 1

    return cnt


print(solution(n))

[
    [0, 0, 0],
    [0, 0, 1],
    [0, 2, 0]
]
