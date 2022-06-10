n, k = map(int, input().split(' '))


def solution(n, k):
    if n == k:
        print(0)
        print(n)
        return

    dp = [[float("inf"), None] for _ in range(200001)]
    dp[n] = [0, None]
    queue = [n]

    while queue:
        pop = queue.pop(0)
        if pop - 1 >= 0:
            if dp[pop - 1][0] > dp[pop][0] + 1:
                dp[pop - 1][0] = dp[pop][0] + 1
                dp[pop - 1][1] = pop
                queue.append(pop - 1)
        if pop + 1 <= 200000:
            if dp[pop + 1][0] > dp[pop][0] + 1:
                dp[pop + 1][0] = dp[pop][0] + 1
                dp[pop + 1][1] = pop
                queue.append(pop + 1)

        if pop * 2 <= 200000:
            if dp[pop * 2][0] > dp[pop][0] + 1:
                dp[pop * 2][0] = dp[pop][0] + 1
                dp[pop * 2][1] = pop
                queue.append(pop * 2)

    location = k
    path = []

    while location != n:
        path.append(dp[location][1])
        location = dp[location][1]

    path = list(reversed(path))
    path.append(k)

    print(dp[k][0])
    print(' '.join(map(str, path)))


solution(n, k)
