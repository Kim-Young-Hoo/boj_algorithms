import sys
from collections import deque

n = int(input())
lst = deque(sorted(list(map(int, input().split(' ')))))

current_limit = 0
while lst:
    pop = lst.popleft()
    if pop - current_limit > 1:
        print(current_limit + 1)
        sys.exit()
    else:
        current_limit += pop
print(current_limit + 1)
