import heapq

t = int(input())

for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split(' ')))
    heapq.heapify(lst)

    res = 0
    while len(lst) > 2:
        a = heapq.heappop(lst)
        b = heapq.heappop(lst)
        res += a + b
        heapq.heappush(lst, a + b)
    res += sum(lst)
    print(res)
