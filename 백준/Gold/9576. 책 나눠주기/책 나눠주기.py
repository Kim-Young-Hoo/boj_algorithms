t = int(input())

for _ in range(t):
    n, m = map(int, input().split(' '))
    lst = []
    for _ in range(m):
        a, b = map(int, input().split(' '))
        lst.append([a, b, b - a])

    lst.sort(key=lambda x: (x[1]))
    check = [0] * (n + 1)
    cnt = 0
    for i in range(m):
        a, b, c = lst[i]

        for j in range(a, b + 1):
            if not check[j]:
                check[j] = 1
                cnt += 1
                break
    print(cnt)
