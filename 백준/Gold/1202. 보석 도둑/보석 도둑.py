import sys
import heapq
from collections import deque

n, k = map(int, input().split(' '))

jewels = []
for i in range(n):
    jewels.append(list(map(int, sys.stdin.readline().split())))
jewels = sorted(jewels)

bags = []
for i in range(k):
    heapq.heappush(bags, int(sys.stdin.readline()))


def solution(jewels, bags):
    cnt = 0
    jewel_heap = []

    while bags:
        bag = heapq.heappop(bags)

        while jewels and bag >= jewels[0][0]:
            heapq.heappush(jewel_heap, -jewels[0][1])
            heapq.heappop(jewels)

        if jewel_heap:
            cnt += heapq.heappop(jewel_heap)
        elif not jewels:
            break
    return -cnt


print(solution(jewels, bags))
