import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))


def solution(heap):
    
    if len(heap) == 1:
        return 0
    
    cnt = 0

    while heap:
        first_pop = heapq.heappop(heap)
        second_pop = heapq.heappop(heap)
        sum_of_pop = first_pop + second_pop
        if heap:
            heapq.heappush(heap, sum_of_pop)
        cnt += sum_of_pop
    return cnt


print(solution(heap))
