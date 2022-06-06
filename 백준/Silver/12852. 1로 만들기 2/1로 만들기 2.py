import heapq

n = int(input())


def sol(n):
    res = [(0, None), (0, None), (1, 1), (1, 1)]

    # if n < 4:
    #     return res[n]

    for i in range(4, n + 1):
        heap = []
        heapq.heappush(heap, (res[i - 1][0] + 1, i - 1))
        if i % 3 == 0:
            heapq.heappush(heap, (res[i // 3][0] + 1, i // 3))
        if i % 2 == 0:
            heapq.heappush(heap, (res[i // 2][0] + 1, i // 2))
        res.append(heapq.heappop(heap))

    lst = [n]
    location = n
    while location:
        lst.append(res[location][1])
        location = res[location][1]

    print(res[n][0])
    print(' '.join(map(str, lst[:-1])))


sol(n)
