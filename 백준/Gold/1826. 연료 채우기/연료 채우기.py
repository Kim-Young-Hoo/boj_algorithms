import heapq
import random


n = int(input())

stations = []
for _ in range(n):
    stations.append(list(map(int, input().split(' '))))

dest, fuel = map(int, input().split(' '))
stations = sorted(stations, key=lambda x: x[0])



# n = random.randrange(1, 20)
# stations = []
# for _ in range(n):
#     stations.append([random.randrange(1, 200), random.randrange(1, 200)])
# dest, fuel = random.randrange(300, 500), random.randrange(1, 100)
#
# print(n)
# print(stations)
# print(sum([station[1] for station in stations]))
# print(dest, fuel)


def solution(stations, dest, fuel):

    heap = []
    cnt = 0

    while True:
        while stations:
            pop = stations.pop(0)
            if pop[0] <= fuel:
                heapq.heappush(heap, -pop[1])
            else:
                stations.insert(0, pop)
                break

        if len(heap) == 0:
            return -1

        if fuel >= dest:
            break

        current_max = -heapq.heappop(heap)
        fuel += current_max
        cnt += 1


    return cnt


print(solution(stations, dest, fuel))



