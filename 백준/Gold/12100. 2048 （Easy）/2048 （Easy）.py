from pprint import pprint

n = int(input())

_matrix = []
for _ in range(n):
    _matrix.append(list(map(int, input().split(' '))))

max_num = 0


def rotate_matrix(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


def solution(matrix, cnt=5):
    global n
    global max_num

    if cnt == 0:
        for i in range(n):
            for j in range(n):
                max_num = max(max_num, matrix[i][j])
        return

    for _ in range(4):
        # print(matrix)
        transpose = rotate_matrix(matrix)
        # print(transpose)
        new_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[i][j] = transpose[i][j]
        matrix = new_matrix

        for i in range(n):
            zero_cnt = 0
            elements = []
            for j in range(n):
                if transpose[i][j] == 0:
                    zero_cnt += 1
                else:
                    elements.append(transpose[i][j])
            elements.extend([0] * zero_cnt)
            transpose[i] = elements

        idx = 0
        while idx < n - 1:
            for row in range(n):
                if transpose[row][idx] == transpose[row][idx + 1]:
                    transpose[row][idx] = transpose[row][idx] * 2
                    transpose[row].pop(idx + 1)
                    transpose[row].append(0)
            idx += 1
        solution(transpose, cnt - 1)


solution(_matrix, 5)
print(max_num)
