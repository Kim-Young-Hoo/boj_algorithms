n, k = map(int, input().split(' '))


def solution(n, k):
    dp = [float("inf")] * 100001
    queue = [n]
    dp[n] = 0

    while queue:
        pop = queue.pop(0)
        if pop - 1 >= 0:
            if dp[pop - 1] > dp[pop] + 1:
                dp[pop - 1] = dp[pop] + 1
                queue.append(pop - 1)
        if pop + 1 <= 100000:
            if dp[pop + 1] > dp[pop] + 1:
                dp[pop + 1] = dp[pop] + 1
                queue.append(pop + 1)
        if pop * 2 <= 100000:
            if dp[pop * 2] > dp[pop]:
                dp[pop * 2] = dp[pop]
                queue.append(pop * 2)

    return dp[k]


print(solution(n, k))
