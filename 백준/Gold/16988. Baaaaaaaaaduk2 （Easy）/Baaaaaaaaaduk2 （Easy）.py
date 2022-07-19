import sys
from collections import deque
from itertools import combinations

n, m = map(int, input().split(' '))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

d = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def dfs(x, y, idx):
    stack = deque([(x, y)])
    cnt = 0
    near_zeros = []
    while stack:
        x, y = stack.pop()
        cnt += 1
        matrix[x][y] = idx

        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == 2:
                    stack.append((nx, ny))
                    matrix[nx][ny] = idx
                elif matrix[nx][ny] == 0 and (nx, ny) not in near_zeros:
                    near_zeros.append((nx, ny))

    return cnt, near_zeros

possible_spots = []
idx = 3
dfs_start_spot = []
cluster_size = []
cluster_near_zeros = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            cnt, near_zeros = dfs(i, j, idx)
            dfs_start_spot.append((i, j))
            cluster_size.append(cnt)
            cluster_near_zeros.append(near_zeros)
            idx += 1
        elif matrix[i][j] == 0:
            for dx, dy in d:
                nx, ny = i + dx, j + dy

                if 0 <= nx < n and 0 <= ny < m:
                    if matrix[nx][ny] not in (0, 1) and (nx, ny) not in possible_spots:
                        possible_spots.append((i, j))
                        break



if len(possible_spots) >= 2:
    comb = combinations(possible_spots, 2)
elif len(possible_spots) == 1:
    comb = [[possible_spots[0]]]
else:
    print(sum(cluster_size))
    sys.exit()
max_cnt = 0

# print(possible_spots)
# print(list(comb))


for c in comb:
    cnt = 0
    idx = 0
    for near_zeros in cluster_near_zeros:
        near_zeros_cnt = len(near_zeros)

        for spot in near_zeros:
            if spot in c:
                near_zeros_cnt -= 1

        if near_zeros_cnt == 0:
            cnt += cluster_size[idx]
        idx += 1
    max_cnt = max(max_cnt, cnt)

print(max_cnt)
