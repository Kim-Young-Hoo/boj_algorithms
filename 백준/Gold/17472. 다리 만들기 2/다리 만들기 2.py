from itertools import combinations

n, m = map(int, input().split(' '))

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(' '))))



def solution(n, m, matrix):
    # 섬 구해놓기
    min_res = float("inf")
    islands = {}
    visited = []
    island_cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and (i, j) not in visited:
                coords = bfs(n, m, matrix, (i, j))
                visited.extend(coords)
                islands[island_cnt] = coords
                island_cnt += 1


    # 각 섬을 잇는 최소 다리 찾기
    bridges = {} # (섬, 섬): [(다리 좌표), (다리 좌표), 다리 길이]
    for island_from in range(len(islands)):
        for start in islands[island_from]:
            for island_to in range(island_from+1, len(islands)):
                hor_bridge = []
                ver_bridge = []
                for end in islands[island_to]:
                    if start[0] == end[0]:    # 행이 같은 경우
                        hor_bridge.append(end)
                    if start[1] == end[1]:
                        ver_bridge.append(end)
                min_hor_bridge = (float("inf"), float("inf"))
                for bridge in hor_bridge:
                    if abs(start[1] - bridge[1]) < min_hor_bridge[1]:
                        if sum([matrix[start[0]][j] for j in range(min(start[1], bridge[1]) + 1, max(start[1], bridge[1]))]) == 0:
                            min_hor_bridge = bridge

                min_ver_bridge = (float("inf"), float("inf"))
                for bridge in ver_bridge:
                    if abs(start[0] - bridge[0]) < min_ver_bridge[0]:
                        if sum([matrix[i][start[1]] for i in range(min(start[0], bridge[0])+1, max(start[0], bridge[0]))]) == 0:
                            min_ver_bridge = bridge

                if min_hor_bridge[1] != float("inf") and abs(start[1] - min_hor_bridge[1]) > 2:

                    if (island_from, island_to) in bridges.keys():
                        if bridges[(island_from, island_to)][2] > abs(start[1] - min_hor_bridge[1]) - 1:
                            bridges[(island_from, island_to)] = [start, min_hor_bridge, abs(start[1] - min_hor_bridge[1])-1]
                    else:
                        bridges[(island_from, island_to)] = [start, min_hor_bridge, abs(start[1] - min_hor_bridge[1])-1]

                if min_ver_bridge[0] != float("inf") and abs(start[0] - min_ver_bridge[0]) > 2:

                    if (island_from, island_to) in bridges.keys():
                        if bridges[(island_from, island_to)][2] > abs(start[0] - min_ver_bridge[0]) - 1:
                            bridges[(island_from, island_to)] = [start, min_ver_bridge, abs(start[0] - min_ver_bridge[0])-1]
                    else:
                        bridges[(island_from, island_to)] = [start, min_ver_bridge, abs(start[0] - min_ver_bridge[0])-1]

    # 각 다리에서 1개씩 제외해서 연결 가능한지 보고 가능하면 min값 업데이트

    idx = 1
    while idx <= len(bridges):
        for c in combinations(bridges, idx):
            cost = 0
            graph = {}

            for start, end in c:
                if start not in graph.keys():
                    graph[start] = [end]
                else:
                    graph[start].append(end)
                if end not in graph.keys():
                    graph[end] = [start]
                else:
                    graph[end].append(start)
                cost += bridges[(start, end)][2]

            queue = [c[0][0]]
            visited = []
            while queue:
                pop = queue.pop(0)
                if pop not in visited:
                    visited.append(pop)
                for node in graph[pop]:
                    if node not in visited:
                        queue.append(node)

            if len(visited) == len(islands):
                min_res = min(min_res, cost)
        idx += 1

    if min_res == float("inf"):
        return -1

    return min_res

def bfs(n, m, matrix, start_node):
    direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    queue = [start_node]
    visited = []

    while queue:
        pop = queue.pop(0)
        if pop not in visited:
            visited.append(pop)

        for dx, dy in direction:
            new_x, new_y = pop[0] + dx, pop[1] + dy
            if 0 <= new_x < n and 0 <= new_y < m:
                if matrix[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                    queue.append((new_x, new_y))

    return visited


print(solution(n, m, matrix))


