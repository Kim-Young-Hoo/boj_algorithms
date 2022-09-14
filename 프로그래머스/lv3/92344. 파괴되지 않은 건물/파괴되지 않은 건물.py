def solution(board, skill):
    answer = 0

    cum_mat = [[0] * (len(board) + 3) for _ in range(len(board) + 3)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == 1:
            degree *= -1

        cum_mat[r1][c1] += degree
        cum_mat[r2 + 1][c1] -= degree
        cum_mat[r1][c2 + 1] -= degree
        cum_mat[r2 + 1][c2 + 1] += degree

    dp = [[0] * (len(board) + 1) for _ in range(len(board) + 1)]
    for i in range(len(board)):
        dp[i][0] = cum_mat[i][0]

    for i in range(len(board)):
        for j in range(1, len(board)):
            dp[i][j] = dp[i][j - 1] + cum_mat[i][j]

    for j in range(len(board)):
        for i in range(1, len(board)):
            dp[i][j] = dp[i - 1][j] + dp[i][j]

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] + dp[i][j] > 0:
                answer += 1

    return answer
