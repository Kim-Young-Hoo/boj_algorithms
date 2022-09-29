def solution(rows, columns, queries):
    matrix = [[0] * columns for _ in range(rows)]
    answer = []


    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = (i * columns) + (j + 1)

    for a, b, c, d, in queries:

        min_val = float("inf")

        print(min_val)

        a -= 1
        b -= 1
        c -= 1
        d -= 1

        temp = None
        for i in range(a, c + 1):
            if i == a:
                temp = matrix[a][d]
                for j in reversed(range(b + 1, d + 1)):
                    matrix[i][j] = matrix[i][j - 1]
                    min_val = min(min_val, matrix[i][j])

                matrix[a][b] = matrix[a + 1][b]
                min_val = min(min_val, matrix[a][b])
            elif i == c:
                for j in range(b, d):
                    matrix[i][j] = matrix[i][j + 1]
                    min_val = min(min_val, matrix[i][j])

                matrix[c][d] = temp
                min_val = min(min_val, matrix[c][d])
            else:
                matrix[i][b] = matrix[i + 1][b]
                min_val = min(min_val, matrix[i][b])
                new_temp = matrix[i][d]
                matrix[i][d] = temp
                temp = new_temp
                min_val = min(min_val, matrix[i][d])
        answer.append(min_val)

    return answer
