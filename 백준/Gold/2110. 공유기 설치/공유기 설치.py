import sys

n, m = map(int, input().split(' '))
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))


def solution(n, m, lst):
    lst = sorted(lst)
    left = 1
    right = lst[-1] - lst[0]

    max_dist = 0

    while left <= right:
        mid = (left + right) // 2

        current_house = lst[0]
        cnt = 1

        for i in range(1, len(lst)):
            if lst[i] - current_house >= mid:
                cnt += 1
                current_house = lst[i]

        if cnt >= m:
            left = mid + 1
            max_dist = mid
        else:
            right = mid - 1

    return max_dist


print(solution(n, m, lst))
