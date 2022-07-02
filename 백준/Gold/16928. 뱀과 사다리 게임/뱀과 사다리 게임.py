n, m = map(int, input().split(' '))

dp = [float("inf")] * 101

ladders_snakes = {}
for _ in range(n):
    a, b = map(int, input().split(' '))
    ladders_snakes[a] = b

for _ in range(m):
    a, b = map(int, input().split(' '))
    ladders_snakes[a] = b


def solution():
    stack = [(1, 0)]

    while stack:
        node, depth = stack.pop()

        if depth < dp[node]:
            dp[node] = depth
        else:
            continue

        if node in ladders_snakes.keys():
            stack.append((ladders_snakes[node], depth))

        else:
            for i in range(1, 7):
                if node + i <= 100:
                    stack.append((node + i, depth + 1))

    return dp[100]


print(solution())
