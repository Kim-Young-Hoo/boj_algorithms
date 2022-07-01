r, c = map(int, input().split(' '))
matrix = []
for _ in range(r):
    matrix.append(list(input()))

max_val = 0
direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def solution(x, y, check, depth):
    global max_val
    global r
    global c

    max_val = max(max_val, depth)

    for dx, dy in direction:
        new_x, new_y = x + dx, y + dy

        if 0 <= new_x < r and 0 <= new_y < c:
            new_char = ord(matrix[new_x][new_y]) - 65
            if not check[new_char]:
                check[new_char] = 1
                solution(new_x, new_y, check, depth + 1)
                check[new_char] = 0

check = [0] * 26
check[ord(matrix[0][0]) - 65] = 1

solution(0, 0, check, 1)
print(max_val)