n, r, c = map(int, input().split(' '))


def solution(n, r, c):
    if n == 1:
        if r == 0 and c == 0:
            return 0
        elif r == 0 and c == 1:
            return 1
        elif r == 1 and c == 0:
            return 2
        elif r == 1 and c == 1:
            return 3

    if n > 1:
        a, b = 1 if r // (2 ** (n - 1)) == 0 else 2, 1 if c // (2 ** (n - 1)) == 0 else 2
        if a == 1 and b == 1:
            multiplier = 0
        elif a == 1 and b == 2:
            multiplier = 1
        elif a == 2 and b == 1:
            multiplier = 2
        else:
            multiplier = 3
        return (multiplier * ((2 ** (n - 1)) ** 2)) + solution(n - 1, r % (2 ** (n - 1)), c % (2 ** (n - 1)))


print(solution(n, r, c))
