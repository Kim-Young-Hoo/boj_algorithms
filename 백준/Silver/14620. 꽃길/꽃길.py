n = int(input())

check = [[0] * n for _ in range(n)]
price = [[0] * n for _ in range(n)]

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

dx = [0, 1, -1, 0, 0]
dy = [1, 0, 0, -1, 0]

pos = []

for i in range(1, n - 1):
    for j in range(1, n - 1):
        for k in range(5):
            nx, ny = i + dx[k], j + dy[k]
            price[i][j] += matrix[nx][ny]
        pos.append([i, j])

from itertools import combinations

min_val = float("inf")

for c in combinations(pos, 3):
    possible = True
    lst = list(c)
    current_sum = 0

    for i in range(3):
        for j in range(i + 1, 3):
            if lst[i][0] == lst[j][0] and abs(lst[i][1] - lst[j][1]) < 3:
                possible = False
            if lst[i][1] == lst[j][1] and abs(lst[i][0] - lst[j][0]) < 3:
                possible = False
            if abs(lst[i][0] - lst[j][0]) + abs(lst[i][1] - lst[j][1]) == 2:
                possible = False

    if possible:
        for x, y in lst:
            current_sum += price[x][y]
        min_val = min(min_val, current_sum)

print(min_val)
