import sys

n, m = map(int, input().split(' '))

lst = list(map(int, input().split(' ')))


def solution(n, m, lst):
    lst = sorted(lst)
    left = 0
    right = lst[-1]

    while left <= right:

        mid = (left + right) // 2
        current_sum = sum([ele - mid for ele in lst if ele - mid >= 0])
        if current_sum >= m:
            left = mid + 1
        else:
            right = mid - 1

    return right


print(solution(n, m, lst))
