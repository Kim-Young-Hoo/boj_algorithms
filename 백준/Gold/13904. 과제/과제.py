"""
job sequencing with deadlines
"""


n = int(input())
lst = []

max_day = 0

for _ in range(n):
    a, b = map(int, input().split(' '))
    max_day = max(max_day, a)
    lst.append([a, b])

lst.sort(key=lambda x: (x[1]), reverse=True)

check = [0] * (max_day + 1)

for i in range(n):
    deadline, profit = lst[i]
    if not check[deadline]:
        check[deadline] = profit
    else:
        for another_deadline in range(deadline - 1, 0, -1):
            if not check[another_deadline]:
                check[another_deadline] = profit
                break

print(sum(check))