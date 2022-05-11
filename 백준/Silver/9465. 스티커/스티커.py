"""
max(이전 열의 대각 요소 + 자기, 전전 열의 max() + 자기)
"""



t = int(input())


def solution(n):
    for i in range(2, n):
        prev_prev_max = max(dp[0][i - 2], dp[1][i - 2])
        dp[0][i] = max(matrix[0][i] + dp[1][i-1], matrix[0][i] + prev_prev_max)
        dp[1][i] = max(matrix[1][i] + dp[0][i-1], matrix[1][i] + prev_prev_max)

    max_val = 0
    for i in range(2):
        for j in range(n):
            max_val = max(dp[i][j], max_val)

    return max_val

for _ in range(t):
    n = int(input())

    matrix = []
    for _ in range(2):
        matrix.append(list(map(int, input().split(' '))))

    if n == 1:
        print(max(matrix[0][0], matrix[1][0]))
        continue


    dp = [[0] * n for _ in range(2)]

    dp[0][0] = matrix[0][0]
    dp[1][0] = matrix[1][0]

    dp[0][1] = matrix[0][1] + dp[1][0]
    dp[1][1] = matrix[1][1] + dp[0][0]

    print(solution(n))

