import sys

sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split(' '))))

blank = []

for i in range(9):
    for j in range(9):
        if not sudoku[i][j]:
            blank.append([i, j])

def solution(matrix, idx):

    if idx == len(blank):
        for row in matrix:
            print(*row)
        sys.exit(0)

    i, j = blank[idx]
    for num in range(1, 10):
        # 가로 체크
        if num in matrix[i]:
            continue
        # 세로 체크
        if num in [ele[j] for ele in matrix]:
            continue
        # 사각형 체크
        sub_lst = []
        for sub_i in range(i // 3 * 3, i // 3 * 3 + 3):
            for sub_j in range(j // 3 * 3, j // 3 * 3 + 3):
                sub_lst.append(matrix[sub_i][sub_j])
        if num in sub_lst:
            continue

        matrix[i][j] = num
        solution(matrix, idx + 1)
        matrix[i][j] = 0



solution(sudoku, 0)
