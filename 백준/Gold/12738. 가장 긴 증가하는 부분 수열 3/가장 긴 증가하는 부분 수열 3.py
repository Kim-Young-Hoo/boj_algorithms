import sys

n = int(input())
lst = list(map(int, sys.stdin.readline().split()))

current_seq = [lst[0]]


def check(mid, i):
    return current_seq[mid] >= lst[i]


for i in range(1, n):
    if current_seq[-1] < lst[i]:
        current_seq.append(lst[i])

    else:
        left = 0
        right = len(current_seq) - 1
        while left <= right:
            mid = (left + right) // 2

            if check(mid, i):
                right = mid - 1
            else:
                left = mid + 1
        if current_seq[left] != lst[i]:
            current_seq[left] = lst[i]

print(len(current_seq))
