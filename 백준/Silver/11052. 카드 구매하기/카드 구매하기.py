n = int(input())
lst = list(map(int, input().split(' ')))
lst.insert(0, 0)

dp = [0] * (n + 1)
dp[1] = lst[1]

if n == 1:
    print(lst[1])
    import sys

    sys.exit()


def solution(remain):

    if dp[remain]:
        return dp[remain]

    temp = [lst[remain]]
    for i in range(1, remain):
        temp.append(solution(i) + solution(remain - i))
    dp[remain] = max(temp)
    return dp[remain]


print(solution(n))
