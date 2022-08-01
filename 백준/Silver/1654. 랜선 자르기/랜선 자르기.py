"""
k보다 많거나 같다면, mid를 키워야됨
k보다 작다면, mid를 작게해야됨
"""

import sys

k, n = map(int, input().split(' '))
lst = []
for _ in range(k):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()

start = 1
end = lst[-1]


def decision(h, n):
    return sum([ele // h for ele in lst]) >= n


while start <= end:
    mid = (start + end) // 2

    if decision(mid, n):
        start = mid + 1
    else:
        end = mid - 1

print(end)
