n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

dp = [[0] * (2 ** n) for _ in range(n)]

min_sum = float("inf")


def solution(start, current, visited):

    if visited == 2**n - 1:
        if matrix[current][start] > 0:
            return matrix[current][start]
        else:
            return float("inf")

    if dp[current][visited] != 0:
        return dp[current][visited]

    dp[current][visited] = float("inf")

    for i in range(n):
        if (visited & 1 << i) > 0 or matrix[current][i] == 0:
            continue
        current_min = solution(start, i, visited | 1 << i) + matrix[current][i]
        dp[current][visited] = min(dp[current][visited], current_min)

    return dp[current][visited]


print(solution(start=0, current=0, visited=1 << 0))