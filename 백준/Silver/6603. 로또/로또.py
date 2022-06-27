from itertools import combinations
import sys


while True:
    lst = list(map(int, sys.stdin.readline().split()))
    if len(lst) == 1:
        break

    k = lst.pop(0)

    for c in combinations(lst, 6):
        print(*list(c))
    print("")