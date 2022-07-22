import sys
from collections import deque

n, m = map(int, input().split(' '))

matrix = []
for _ in range(n):
    matrix.append(list(input()))


def solution():
    global n, m

    shape = {"\\": 0, "/": 1}

    dp = [[[float("inf")] * 2 for _ in range(m)] for _ in range(n)]
    if matrix[0][0] == "/":
        dp[0][0][0] = 1
        matrix[0][0] = "\\"
    else:
        dp[0][0][0] = 0

    # if matrix[-1][-1] == "/":
    #     matrix[-1][-1] = "\\"

    queue = deque([(0, 0, shape[matrix[0][0]], dp[0][0][0])])

    d = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, 1], [1, -1], [1, 1], [-1, -1]]

    while queue:
        x, y, current_shape, cost = queue.popleft()


        for dx, dy in d:
            current_cost = cost
            nx, ny = dx + x, dy + y

            if 0 <= nx < n and 0 <= ny < m:
                is_one = False
                next_shape = shape[matrix[nx][ny]]
                if current_shape == 0:
                    if (dx, dy) in [(-1, 1), (1, -1)]:
                        continue
                    if (dx, dy) in [(-1, -1), (1, 1)] and shape[matrix[nx][ny]] == 1:
                        current_cost += 1
                        next_shape = 0
                        is_one = True
                    elif (dx, dy) not in [(-1, -1), (1, 1)] and shape[matrix[nx][ny]] == 0:
                        current_cost += 1
                        next_shape = 1
                        is_one = True
                else:
                    if (dx, dy) in [(1, 1), (-1, -1)]:
                        continue
                    if (dx, dy) in [(-1, 1), (1, -1)] and shape[matrix[nx][ny]] == 0:
                        current_cost += 1
                        next_shape = 1
                        is_one = True
                    elif (dx, dy) not in [(-1, 1), (1, -1)] and shape[matrix[nx][ny]] == 1:
                        current_cost += 1
                        next_shape = 0
                        is_one = True

                if dp[nx][ny][next_shape] > current_cost:
                    dp[nx][ny][next_shape] = current_cost
                    if is_one:
                        queue.append((nx, ny, next_shape, current_cost))
                    else:
                        queue.appendleft((nx, ny, shape[matrix[nx][ny]], current_cost))
    return dp[-1][-1][shape["\\"]]


res = solution()
if res == float("inf"):
    print("NO SOLUTION")
else:
    print(res)
