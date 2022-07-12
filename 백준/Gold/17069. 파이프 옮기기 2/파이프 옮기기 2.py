from collections import deque

n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))


def solution():
    global n
    dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]  # right, down, diagonal 순
    dp[0][1][0] = 1

    for x in range(n):
        for y in range(n):
       
            if not matrix[x][y]:
                if 0 <= x - 1 and 0 <= y - 1:
                    if not matrix[x - 1][y] and not matrix[x][y - 1]:
                        dp[x][y][2] += sum(dp[x - 1][y - 1])

                if 0 <= x - 1:
                    dp[x][y][1] += dp[x - 1][y][1] + dp[x - 1][y][2]

                if 0 <= y - 1:
                    dp[x][y][0] += dp[x][y - 1][0] + dp[x][y - 1][2]

    return sum(dp[-1][-1])


print(solution())
