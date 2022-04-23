import sys

n = int(input())
lst = list(map(int, input().split(' ')))
m = int(input())


def solution(n, m, lst):
    lst = sorted(lst)
    left = 0
    right = lst[-1]

    while left <= right:
        mid = (left + right) // 2
        current_sum = 0

        for ele in lst:
            if ele <= mid:
                current_sum += ele
            else:
                current_sum += mid

        if current_sum > m:
            right = mid - 1
        else:
            left = mid + 1
    return right


print(solution(n, m, lst))
