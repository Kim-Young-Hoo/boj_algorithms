t = int(input())


def solution(cost_list, graph, w):
    global dp

    if dp[w] != -1:
        return

    if not graph[w]:
        dp[w] = cost_list[w - 1]
        return

    for ele in graph[w]:

        if dp[ele] != -1:
            dp[w] = max(dp[w], dp[ele] + cost_list[w-1])
        else:
            solution(cost_list, graph, ele)
            dp[w] = max(dp[w], dp[ele] + cost_list[w-1])


for i in range(t):

    n, k = list(map(int, input().split(' ')))
    cost_list = list(map(int, input().split(' ')))
    graph = {}

    for i in range(k + 1):
        graph[i + 1] = []

    for i in range(k):
        start, end = list(map(int, input().split(' ')))
        graph[end].append(start)
    w = int(input())

    dp = {ele + 1: -1 for ele in range(len(graph))}

    solution(cost_list, graph, w)
    print(dp[w])
