import heapq
import sys

n = int(input())

max_heap = []
min_heap = []

first = int(sys.stdin.readline())
second = int(sys.stdin.readline())

print(first)
if first <= second:
    heapq.heappush(max_heap, -1 * first)
    heapq.heappush(min_heap, second)
    print(first)
else:
    heapq.heappush(min_heap, first)
    heapq.heappush(max_heap, -1 * second)
    print(second)

for i in range(n - 2):
    num: int = int(sys.stdin.readline())

    heapq.heappush(min_heap, num)
    heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if len(min_heap) == len(max_heap):
        print(max_heap[0] * -1)
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(max_heap))
        print(max_heap[0] * -1)
    else:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
        print(min_heap[0])

