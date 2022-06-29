n, m = map(int, input().split(' '))

coin1_pos = None
coin2_pos = None

matrix = []
for i in range(n):
    temp = list(input())

    if temp.count("o") == 1:
        if "o" in temp and not coin1_pos:
            coin1_pos = (i + 1, temp.index("o") + 1)
        elif "o" in temp and coin1_pos:
            coin2_pos = (i + 1, temp.index("o") + 1)
    elif temp.count("o") == 2:
        for j in range(len(temp)):
            if temp[j] == "o" and not coin1_pos:
                coin1_pos = (i + 1, j + 1)
            elif temp[j] == "o" and coin1_pos:
                coin2_pos = (i + 1, j + 1)
    temp.insert(0, "x")
    temp.append("x")
    matrix.append(temp)

matrix.insert(0, ["x"] * len(matrix[0]))
matrix.append(["x"] * len(matrix[0]))

min_cnt = float("inf")

n += 2
m += 2


def solution(coin1_pos, coin2_pos, cnt):
    global min_cnt
    global n
    global m

    if coin1_pos == coin2_pos:
        return

    if cnt > 10:
        return

    if matrix[coin1_pos[0]][coin1_pos[1]] == "x" and matrix[coin2_pos[0]][coin2_pos[1]] != "x":
        min_cnt = min(min_cnt, cnt)
        return
    elif matrix[coin1_pos[0]][coin1_pos[1]] != "x" and matrix[coin2_pos[0]][coin2_pos[1]] == "x":
        min_cnt = min(min_cnt, cnt)
        return
    elif matrix[coin1_pos[0]][coin1_pos[1]] == "x" and matrix[coin2_pos[0]][coin2_pos[1]] == "x":
        return

    for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        new_coin1_pos = (coin1_pos[0] + x, coin1_pos[1] + y)
        new_coin2_pos = (coin2_pos[0] + x, coin2_pos[1] + y)

        if 0 <= new_coin1_pos[0] < n and 0 <= new_coin1_pos[1] < m and 0 <= new_coin2_pos[0] < n and 0 <= new_coin2_pos[1] < m:

            if matrix[new_coin1_pos[0]][new_coin1_pos[1]] == "#":
                new_coin1_pos = coin1_pos
            if matrix[new_coin2_pos[0]][new_coin2_pos[1]] == "#":
                new_coin2_pos = coin2_pos

            solution(new_coin1_pos, new_coin2_pos, cnt + 1)


solution(coin1_pos, coin2_pos, 0)

if min_cnt == float("inf"):
    print(-1)
else:
    print(min_cnt)