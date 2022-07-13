n, m = map(int, input().split(' '))


lst = []
for _ in range(n):
    lst.append(input())

lst = set(lst)

cnt = 0

for _ in range(m):
    string = input()
    if string in lst:
        cnt += 1

print(cnt)