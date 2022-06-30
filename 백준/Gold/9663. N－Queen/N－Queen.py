n = int(input())
cnt = 0


def solution(n, row, columns):
    global cnt

    if row == n:
        cnt += 1
        return

    for column in range(n):
        is_possible = True
        if columns[column] == -1:
            for previous_column in range(n):
                if columns[previous_column] != -1:
                    if abs(columns[previous_column] - row) == abs(previous_column - column):
                        is_possible = False
                        break

            if is_possible:
                new_columns = [ele for ele in columns]
                new_columns[column] = row
                solution(n, row + 1, new_columns)


solution(n, 0, [-1] * n)
print(cnt)
