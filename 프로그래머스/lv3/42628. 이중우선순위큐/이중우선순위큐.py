import heapq

def solution(operations):
    answer = []
    min_heap = []
    max_heap = []
    
    for operation in operations:
        operation = operation.split(' ')
        if operation[0] == "I":
            heapq.heappush(min_heap, int(operation[1]))
            heapq.heappush(max_heap, -int(operation[1]))
        else:
            if min_heap:
                if operation[1] == "1":
                    pop = -heapq.heappop(max_heap)
                    min_heap.remove(pop)
                else:
                    pop = heapq.heappop(min_heap)
                    max_heap.remove(-pop)
    
    if min_heap:
        return [-heapq.heappop(max_heap), heapq.heappop(min_heap)]
    else:
        return [0, 0]

