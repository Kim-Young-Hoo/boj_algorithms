import heapq
import sys

n = int(input())

lst = []
for _ in range(n):
    heapq.heappush(lst, list(map(int, sys.stdin.readline().split())))

lst.sort(key=lambda x: x[0])

left, right = lst[0]
answer = 0

for i in range(1, n):
    cur_left, cur_right = lst[i]

    if cur_left > right:
        answer += right - left
        left = cur_left
        right = cur_right
    else:
        if cur_right > right:
            right = cur_right

answer += right - left
print(answer)