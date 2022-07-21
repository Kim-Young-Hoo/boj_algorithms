a_limit, b_limit, c_limit = map(int, input().split(' '))

visited = [[0] * 201 for _ in range(201)]
answer = [0] * (c_limit + 1)


def sol(a, b, c):
    global a_limit, b_limit, c_limit

    if a > a_limit or b > b_limit or c > c_limit:
        return

    if a < 0 or b < 0 or c < 0:
        return

    if visited[a][b]:
        return

    visited[a][b] = 1
    if a == 0:
        answer[c] = 1


    # a를 b에다가
    # 넘쳐
    if b + a > b_limit:
        temp = b + a - b_limit
        sol(temp, b + a - temp, c)
    # 안넘쳐
    else:
        sol(0, a + b, c)

    # a를 c에다가 부어줌
    if c + a > c_limit:
        temp = c + a - c_limit
        sol(temp, b, c + a - temp)
    else:
        sol(0, b, a + c)

    # b를 c에다가 부어
    if c + b > c_limit:
        temp = c + b - c_limit
        sol(a, temp, c + b - temp)
    else:
        sol(a, 0, c + b)

    # b를 a에다가
    if b + a > a_limit:
        temp = b + a - a_limit
        sol(a + b - temp, temp, c)
    else:
        sol(a + b, 0, c)

    # c를 a에다가
    if c + a > a_limit:
        temp = c + a - a_limit
        sol(a + c - temp, b, temp)
    else:
        sol(a + c, b, 0)

    # c를 b에다가
    if c + b > b_limit:
        temp = c + b - b_limit
        sol(a, b + c - temp, temp)
    else:
        sol(a, b + c, 0)

sol(0, 0, c_limit)
# answer = sorted(answer)

string = []
for i in range(len(answer)):
    if answer[i]:
        string.append(i)
string = sorted(string)

print(*string)
