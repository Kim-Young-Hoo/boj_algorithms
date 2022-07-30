n = int(input())
lst = list(map(int, input().split(' ')))
arrows = [0] * 1000001
cnt = 0

for i in range(n):
    if arrows[lst[i]]:
        arrows[lst[i] - 1] += 1
        arrows[lst[i]] -= 1
    else:
        arrows[lst[i] - 1] += 1
        cnt += 1

print(cnt)
