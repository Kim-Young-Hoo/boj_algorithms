import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split(' '))

matrix = []
for _ in range(n):
    row = list(input())
    sub_lst = []
    for char in row:
        if char == "H":
            sub_lst.append(char)
        else:
            sub_lst.append(int(char))
    matrix.append(sub_lst)

dp = [[-1] * m for _ in range(n)]
d = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def solution(x, y, cnt):
    global n
    global m

    # 이거 수정해야됨 -> 순회여야 -1임
    if n * m < cnt:
        print(-1)
        sys.exit()

    if dp[x][y] > -1:
        return dp[x][y]

    lst = []
    for dx, dy in d:
        new_x = x + dx * matrix[x][y]
        new_y = y + dy * matrix[x][y]
        if 0 <= new_x < n and 0 <= new_y < m:
            if matrix[new_x][new_y] != "H":
                lst.append(1 + solution(new_x, new_y, cnt + 1))

    if lst:
        dp[x][y] = max(max(lst), dp[x][y])
    else:
        dp[x][y] = 1
        return 1
    return dp[x][y]


solution(0, 0, 1)

print(dp[0][0])

