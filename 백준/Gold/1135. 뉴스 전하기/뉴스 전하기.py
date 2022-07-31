import heapq
from collections import deque

n = int(input())
tree = list(map(int, input().split(' ')))
graph = {i: [] for i in range(n + 1)}

for i in range(1, n):
    graph[tree[i]].append(i)


dp = [0] * n

def solution(current_node):
    if not graph[current_node]:
        return 1
    temp = []
    for next_node in graph[current_node]:
        solution(next_node)
        temp.append(dp[next_node])
    temp = sorted(temp, reverse=True)
    temp = [temp[i] + i + 1 for i in range(len(temp))]
    dp[current_node] = max(temp)


solution(0)
print(dp[0])