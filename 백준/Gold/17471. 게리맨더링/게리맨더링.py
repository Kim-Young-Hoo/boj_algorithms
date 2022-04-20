from itertools import combinations

n = int(input())
population = list(map(int, input().split(' ')))

graph = {}

for i in range(n):
    lst = list(map(int, input().split(' ')))
    graph[i + 1] = lst[1:]


def solution(n, population, graph):
    min_res = float("inf")

    for i in range(n // 2 + 1):
        for section_a in combinations(list(graph.keys()), i):
            section_b = [ele for ele in list(graph.keys()) if ele not in section_a]

            # a 섹션에 대해서 순회
            if section_a:
                queue = [section_a[0]]
                visited = []
                while queue:
                    node = queue.pop(0)

                    if node not in visited:
                        visited.append(node)

                    for adj_node in graph[node]:
                        if adj_node not in section_b and adj_node not in visited:
                            queue.append(adj_node)

                if len(visited) + len(section_b) != n:  # 불가능한 거
                    continue

            # b 섹션 순회
            if section_b:
                queue = [section_b[0]]
                visited = []
                while queue:
                    node = queue.pop(0)

                    if node not in visited:
                        visited.append(node)

                    for adj_node in graph[node]:
                        if adj_node not in section_a and adj_node not in visited:
                            queue.append(adj_node)

                if len(visited) + len(section_a) != n:  # 불가능한 거
                    continue

            a_sum = sum([population[ele - 1] for ele in section_a])
            b_sum = sum([population[ele - 1] for ele in section_b])
            min_res = min(min_res, abs(a_sum - b_sum))

    if min_res == float("inf"):
        return -1
    return min_res


print(solution(n, population, graph))