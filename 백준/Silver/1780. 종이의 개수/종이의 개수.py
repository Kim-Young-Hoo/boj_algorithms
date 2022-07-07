n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

answer = {-1: 0, 0: 0, 1: 0}


def check(x, y, n):
    last = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if last != matrix[i][j]:
                return False
    return True


def solution(x, y, n):
    if n == 1:
        answer[matrix[x][y]] += 1
        return

    if check(x, y, n):
        answer[matrix[x][y]] += 1
        return

    for dx in range(0, n, n // 3):
        for dy in range(0, n, n // 3):
            solution(x + dx, y + dy, n // 3)


solution(0, 0, n)

for key, val in answer.items():
    print(val)

