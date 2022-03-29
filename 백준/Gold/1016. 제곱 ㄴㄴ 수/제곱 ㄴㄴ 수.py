m, n = list(map(int, input().split(' ')))


def solution(m, n):
    lst = [False for i in range(m, n + 1)]
    cnt = n - m + 1

    i = 2
    square_number = i * i
    while square_number <= n:
        remain = 0 if m % square_number == 0 else 1
        j = m // square_number + remain
        while square_number * j <= n:
            if not lst[square_number*j-m]:
                lst[square_number*j-m] = True
                cnt -= 1
            j += 1
        i += 1
        square_number = i * i

    return cnt


print(solution(m, n))
