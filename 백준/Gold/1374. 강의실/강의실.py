import heapq
import sys

n = int(input())
min_heap = []
max_heap = []
cnt = 1

for _ in range(n):
    _, a, b = map(int, sys.stdin.readline().split())
    heapq.heappush(min_heap, [a, b])

heapq.heappush(max_heap, heapq.heappop(min_heap)[1])
while min_heap:
    min_end = heapq.heappop(max_heap)
    a, b = heapq.heappop(min_heap)

    if a >= min_end:
        heapq.heappush(max_heap, b)
    else:
        cnt += 1
        heapq.heappush(max_heap, b)
        heapq.heappush(max_heap, min_end)

print(cnt)