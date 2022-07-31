n = int(input())
lst = list(map(int, input().split(' ')))

least_h = sum(lst) // 3

if sum(lst) % 3 != 0:
    print("NO")

else:
    cnt = 0
    for i in range(n):
        if lst[i] >= 2:
            cnt += lst[i] // 2
    if cnt < least_h:
        print("NO")
    else:
        print("YES")
