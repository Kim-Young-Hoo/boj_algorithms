import heapq


def solution(n, s):
    return func(n, s)


def func(n, s):
    if s < n:
        return [-1]

    answer = [s // n] * (n - (s % n))
    answer.extend([s // n + 1] * (s % n))
    return answer


solution(2, 9)
