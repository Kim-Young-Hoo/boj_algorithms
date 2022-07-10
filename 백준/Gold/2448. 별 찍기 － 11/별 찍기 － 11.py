# matrix = ["*", "* *", "*****"]
#
# # for i in range(len(matrix)):
# #     print(matrix[i])
#
# new_matrix = []
# n = 6
#
# for i in range(2):
#     for j in range(len(matrix)):
#         if i == 0:
#             new_matrix.append(matrix[j])
#         else:
#             new_matrix.append(matrix[j] + " " * ((n - 1) - (j * 2)) + matrix[j])
#
#
# #      *
# #     * *
# #    *****
# #   *     *
# #  * *   * *
# # ***** *****
#
# final_matrix = []
# n = 12
#
# for i in range(2):
#     for j in range(len(new_matrix)):
#         if i == 0:
#             final_matrix.append(new_matrix[j])
#         else:
#             final_matrix.append(new_matrix[j] + " " * ((n - 1) - (j * 2)) + new_matrix[j])
#
# for i in range(len(final_matrix)):
#     print(" " * (n - 1 - i) + final_matrix[i] + " " * (n - 1 - i))
n = int(input())


def solution(n):
    if n == 3:
        return ["*", "* *", "*****"]

    matrix = solution(n // 2)
    new_matrix = []
    for i in range(2):
        for j in range(len(matrix)):
            if i == 0:
                new_matrix.append(matrix[j])
            else:
                new_matrix.append(matrix[j] + " " * ((n - 1) - (j * 2)) + matrix[j])
    return new_matrix


output = solution(n)
for i in range(len(output)):
    print(" " * (n - 1 - i) + output[i] + " " * (n - 1 - i))
