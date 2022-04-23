import sys

n, m = map(int, input().split(' '))

lst = []
for i in range(n):
    lst.append(int(sys.stdin.readline()))


def solution(n, m, lst):
    lst = sorted(lst)
    left = 1
    right = lst[-1]

    while left <= right:

        mid = (left + right) // 2
        current_sum = 0
        for ele in lst:
            current_sum += ele // mid

        if current_sum < m:
            right = mid - 1
        elif current_sum >= m:
            left = mid + 1

    return right


print(solution(n, m, lst))
