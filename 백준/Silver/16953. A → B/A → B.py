a, b = map(int, input().split(' '))

max_cnt = -2


def solution(a, b, cnt):
    global max_cnt

    if a > b:
        return

    if a == b:
        max_cnt = max(max_cnt, cnt)
        return

    solution(a * 2, b, cnt + 1)
    solution(int(str(a) + "1"), b, cnt + 1)


solution(a, b, 0)
print(max_cnt + 1)
