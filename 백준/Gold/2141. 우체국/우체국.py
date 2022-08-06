import sys

n = int(input())

all_sum = 0
lst = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    lst.append([a, b])
    all_sum += b
lst = sorted(lst, key=lambda x: x[0])

current_sum = 0
for i in range(n):
    current_sum += lst[i][1]
    if current_sum >= (all_sum + 1) // 2:
        print(lst[i][0])
        break
