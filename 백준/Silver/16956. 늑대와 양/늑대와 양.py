import sys

n, m = map(int, input().split(' '))

matrix = []
sheep_pos = []
wolf_pos = []

for i in range(n):
    lst = list(input())

    for j in range(m):
        if lst[j] == "S":
            sheep_pos.append([i, j])
        elif lst[j] == "W":
            wolf_pos.append([i, j])
    matrix.append(lst)

d = [[-1, 0], [1, 0], [0, -1], [0, 1]]

for x, y in sheep_pos:
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == "W":
                print(0)
                sys.exit()
            elif matrix[nx][ny] != "S":
                matrix[nx][ny] = "D"


print(1)
for ele in matrix:
    print(''.join(ele))
