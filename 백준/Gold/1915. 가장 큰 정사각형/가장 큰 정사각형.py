n, m = map(int, input().split(' '))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, list(input()))))


answer = 0

dp = [[0] * m for _ in range(n)]
for i in range(n):
    dp[i][0] = matrix[i][0]
    answer = max(dp[i][0], answer)
for j in range(m):
    dp[0][j] = matrix[0][j]
    answer = max(dp[0][j], answer)


for i in range(1, n):
    for j in range(1, m):
        if matrix[i][j]:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        answer = max(dp[i][j], answer)
print(answer ** 2)


