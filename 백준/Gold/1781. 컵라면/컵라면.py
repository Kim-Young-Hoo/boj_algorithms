import heapq
import sys

n = int(input())
max_heap = []

for _ in range(n):
    a, b = list(map(int, sys.stdin.readline().split()))
    heapq.heappush(max_heap, [-a, -b])

a, b = heapq.heappop(max_heap)
current_deadline = -a
heapq.heappush(max_heap, [a, b])

answer = 0

max_heap2 = []

while current_deadline > 0:

    while max_heap:
        deadline, cup = heapq.heappop(max_heap)
        deadline *= -1

        if deadline >= current_deadline:
            heapq.heappush(max_heap2, cup)
        else:
            heapq.heappush(max_heap, [-deadline, cup])
            break

    if max_heap2:
        answer += -heapq.heappop(max_heap2)
    current_deadline -= 1


print(answer)

