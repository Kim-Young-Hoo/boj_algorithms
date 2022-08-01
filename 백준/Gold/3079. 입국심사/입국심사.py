import sys

n, m = map(int, input().split(' '))
lst = []
for _ in range(n):
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort()

start = 1
end = m * lst[-1]


def decision(t):
    global m
    return sum([t // ele for ele in lst]) < m


while start <= end:
    mid = (start + end) // 2

    if decision(mid):
        start = mid + 1
    else:
        end = mid - 1

print(start)
