import sys

n, c = map(int, input().split(' '))
m = int(input())
lst = []

for _ in range(m):
    lst.append(list(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: (x[1], x[0]))

capacity = [0] * 10001
result = 0
for i in range(m):
    max_cnt = 0
    for j in range(lst[i][0], lst[i][1]):
        max_cnt = max(capacity[j], max_cnt)

    val = min(lst[i][2], c - max_cnt)
    result += val

    for j in range(lst[i][0], lst[i][1]):
        capacity[j] += val

print(result)
