n = int(input())
lst = list(map(int, input().split(' ')))

for i in range(1, n + 1):
    lst[i - 1] = lst[i - 1] * i

for i in reversed(range(1, n)):
    lst[i] -= lst[i - 1]

print(*lst)
