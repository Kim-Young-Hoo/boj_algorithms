from collections import deque

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))


def solution(n, matrix):
    cnt = 0
    stack = deque([[0, 1, "가로"]])

    while stack:
        x, y, direction = stack.pop()

        if (x, y) == (n - 1, n - 1):
            cnt += 1
            continue

        if direction == "가로":
            if 0 <= x + 1 < n and 0 <= y + 1 < n and matrix[x + 1][y + 1] != 1 and matrix[x][y + 1] != 1 and matrix[x + 1][y] != 1:
                stack.append([x + 1, y + 1, "대각"])
            if 0 <= x < n and 0 <= y + 1 < n and matrix[x][y + 1] != 1:
                stack.append([x, y + 1, "가로"])

        elif direction == "세로":
            if 0 <= x + 1 < n and 0 <= y + 1 < n and matrix[x + 1][y + 1] != 1 and matrix[x][y + 1] != 1 and matrix[x + 1][y] != 1:
                stack.append([x + 1, y + 1, "대각"])
            if 0 <= x + 1 < n and 0 <= y < n and matrix[x + 1][y] != 1:
                stack.append([x + 1, y, "세로"])

        else:
            if 0 <= x + 1 < n and 0 <= y + 1 < n and matrix[x + 1][y + 1] != 1 and matrix[x][y + 1] != 1 and matrix[x + 1][y] != 1:
                stack.append([x + 1, y + 1, "대각"])
            if 0 <= x < n and 0 <= y + 1 < n and matrix[x][y + 1] != 1:
                stack.append([x, y + 1, "가로"])
            if 0 <= x + 1 < n and 0 <= y < n and matrix[x + 1][y] != 1:
                stack.append([x + 1, y, "세로"])

    return cnt


print(solution(n, matrix))
