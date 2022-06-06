n = int(input())
lst = list(map(int, input().split(' ')))


def solution(n, lst):
    dp = [[1, -1] for _ in range(n)]

    for i in range(1, n):
        max_idx = -1
        max_len = 0
        for j in range(i):
            if dp[j][0] > max_len and lst[j] < lst[i]:
                max_idx = j
                max_len = dp[j][0]
        dp[i] = [max_len + 1, max_idx]

    max_idx = 0
    max_len = 0
    for i in range(n):
        if dp[i][0] > max_len:
            max_idx = i
            max_len = dp[i][0]
    print(dp[max_idx][0])


    path = []
    location = max_idx
    while location > -1:
        if dp[location][1] > -1:
            path.append(lst[dp[location][1]])
        location = dp[location][1]
    path = list(reversed(path))
    path.append(lst[max_idx])
    print(' '.join(map(str, path)))


solution(n, lst)
