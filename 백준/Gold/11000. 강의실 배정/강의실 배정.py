import heapq
import sys

n = int(input())

lst = []
for _ in range(n):
    heapq.heappush(lst, list(map(int, sys.stdin.readline().split())))

classes = [0]
while lst:
    pop = heapq.heappop(lst)
    changed = False

    class_pop = heapq.heappop(classes)
    if pop[0] >= class_pop:
        heapq.heappush(classes, pop[1])
    else:
        heapq.heappush(classes, class_pop)
        heapq.heappush(classes, pop[1])

print(len(classes))
