from itertools import permutations

n, m, k = map(int, input().split(' '))

matrix = []

for i in range(n):
    matrix.append(list(map(int, input().split(' '))))

args = []
for i in range(k):
    args.append(list(map(int, input().split(' '))))


def solution(n, m, k, matrix, args):
    min_sum = float("inf")
    arg_comb = list(permutations(args))

    for args in arg_comb:
        new_matrix = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                new_matrix[i][j] = matrix[i][j]
        for arg in args:
            new_matrix = rotate(*arg, matrix=new_matrix)


        for row in new_matrix:
            min_sum = min(min_sum, sum(row))

    return min_sum


def rotate(r, c, s, matrix):
    length = int(2 * s)
    up_r_pointer = r - s - 1
    down_r_pointer = r - s - 1 + length

    left_c_pointer = c - s - 1
    right_c_pointer = c - s - 1 + length

    while left_c_pointer != right_c_pointer:
        for i in range(up_r_pointer, down_r_pointer + 1):

            if i < down_r_pointer:
                current_pop = matrix[i].pop(right_c_pointer)
                matrix[i].insert(left_c_pointer, matrix[i + 1].pop(left_c_pointer))
                matrix[i + 1].insert(right_c_pointer - 1, current_pop)

            else:
                matrix[i][right_c_pointer - 1], matrix[i][right_c_pointer] = \
                    matrix[i][
                        right_c_pointer], \
                    matrix[i][
                        right_c_pointer - 1]

        up_r_pointer += 1
        down_r_pointer -= 1
        left_c_pointer += 1
        right_c_pointer -= 1
    return matrix

print(solution(n, m, k, matrix, args))