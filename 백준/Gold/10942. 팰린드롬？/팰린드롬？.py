import sys
sys.setrecursionlimit(10000)


n = int(input())
lst = list(map(int, input().split(' ')))

dp_matrix = [[-1] * n for _ in range(n)]
for i in range(n):
    dp_matrix[i][i] = 1


def solution(s, e):
    if dp_matrix[s][e] == 1:
        return 1
    if dp_matrix[s][e] == 0:
        return 0

    if s >= e:
        return 1

    elif e - s == 2:
        if lst[e] != lst[s]:
            dp_matrix[s][e] = 0
            return 0
        else:
            dp_matrix[s][e] = 1
            return 1

    else:
        if solution(s + 1, e - 1) and lst[s] == lst[e]:
            dp_matrix[s][e] = 1
            return 1
        else:
            dp_matrix[s][e] = 0
            return 0


m = int(input())

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(solution(s - 1, e - 1))

