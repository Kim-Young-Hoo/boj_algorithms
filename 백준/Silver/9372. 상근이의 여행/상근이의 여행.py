import sys

for _ in range(int(input())):
    N, M = map(int, input().split())
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
    print(N-1)
