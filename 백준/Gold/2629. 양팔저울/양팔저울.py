import sys

n = int(input())
lst = list(map(int, input().split(' ')))
m = int(input())
marbles = list(map(int, input().split(' ')))
dp = [[0] * (sum(lst) + 1) for _ in range(n)]

dp[0][0] = 1
dp[0][lst[0]] = 1

for i in range(1, n):
    for j in range(sum(lst) + 1):
        if dp[i - 1][j]:
            if 0 <= abs(j - lst[i]) < sum(lst) + 1:
                dp[i][abs(j - lst[i])] = 1
            if 0 <= j + lst[i] < sum(lst) + 1:
                dp[i][j + lst[i]] = 1
            dp[i][j] = 1


answers = []
for marble in marbles:
    if marble > sum(lst):
        answers.append("N")
    elif dp[-1][marble]:
        answers.append("Y")
    else:
        answers.append("N")

print(' '.join(answers))