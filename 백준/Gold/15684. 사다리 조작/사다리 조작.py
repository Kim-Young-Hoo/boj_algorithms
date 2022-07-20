import sys
from itertools import combinations

n, m, h = map(int, input().split(' '))

original_spot = []

matrix = [[0] * (n + 2) for _ in range(h + 1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    original_spot.append((a, b))
    matrix[a][b] = 1



def solution(start, current_x, current_y):
    global n, m, h

    if current_x == h + 1:
        if current_y == start:
            return True
        else:
            return False

    if matrix[current_x][current_y - 1]:
        return solution(start, current_x + 1, current_y - 1)
    elif matrix[current_x][current_y]:
        return solution(start, current_x + 1, current_y + 1)
    else:
        return solution(start, current_x + 1, current_y)


all_xy = []

for i in range(1, h + 1):
    for j in range(1, n):
        if not matrix[i][j] and not matrix[i][j - 1] and not matrix[i][j + 1]:
            all_xy.append((i, j))

for i in range(0, 4):
    combination = combinations(all_xy, i)
    for comb in combination:
        possible = True
        for j in range(len(comb) - 1):
            if comb[j][0] == comb[j + 1][0] and abs(comb[j][1] - comb[j + 1][1]) == 1:
                possible = False
                break
        if not possible:
            continue

        for x, y in comb:
            matrix[x][y] = 1

        all_passed = True
        for j in range(1, n + 1):
            result = solution(j, 1, j)
            if not result:
                all_passed = False
                break
        if all_passed:
            print(i)
            sys.exit()
        for x, y in comb:
            matrix[x][y] = 0

print(-1)
