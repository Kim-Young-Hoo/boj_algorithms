n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

def solution(n):
    for i in range(n):
        for j in range(n):
            if i == n-1 and j == n-1:
                return dp[n-1][n-1]

            if dp[i][j] > 0:
                if matrix[i][j] + j < n:
                    dp[i][matrix[i][j] + j] += dp[i][j]

                if matrix[i][j] + i < n:
                    dp[matrix[i][j] + i][j] += dp[i][j]


print(solution(n))