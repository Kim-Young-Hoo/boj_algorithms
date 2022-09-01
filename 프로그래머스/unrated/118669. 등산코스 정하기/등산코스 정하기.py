from collections import deque


def solution(n, paths, gates, summits):
    answer = [float("inf"), float("inf")]

    graph = {i: [] for i in range(n + 1)}
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])

    maps = [0] * (n + 1)
    for gate in gates:
        maps[gate] = 1
    for summit in summits:
        maps[summit] = 2
    intensity = [float("inf")] * (n + 1)

    for gate in gates:

        queue = deque([[gate, 0]])

        while queue:
            current_node, current_intensity = queue.pop()

            for node, dist in graph[current_node]:
                new_intensity = max(dist, current_intensity)

                if new_intensity > answer[1]:
                    continue
                if maps[node] == 2:
                    if answer[1] == new_intensity and node < answer[0]:
                        answer = [node, new_intensity]
                    elif answer[1] > new_intensity:
                        answer = [node, new_intensity]
                elif maps[node] == 0 and intensity[node] > new_intensity:
                    if answer[1] >= new_intensity:
                        intensity[node] = new_intensity
                        queue.append([node, new_intensity])
    return answer


print(
    solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
