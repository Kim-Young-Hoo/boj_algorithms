# matrix = ["***", "* *", "***"]
#
# new_matrix = []
#
# for i in range(3):
#     for j in range(len(matrix)):
#         if i == 1:
#             new_matrix.append(matrix[j] + " " * len(matrix) + matrix[j])
#         else:
#             new_matrix.append(matrix[j] * 3)
#
# final_matrix = []
#
# for i in range(3):
#     for j in range(len(new_matrix)):
#         if i == 1:
#             final_matrix.append(new_matrix[j] + " " * len(new_matrix) + new_matrix[j])
#         else:
#             final_matrix.append(new_matrix[j] * 3)
#
# print(final_matrix)
#
# [
#     '***************************',
#     '* ** ** ** ** ** ** ** ** *',
#     '***************************',
#     '***   ******   ******   ***',
#     '* *   * ** *   * ** *   * *',
#     '***   ******   ******   ***',
#     '***************************',
#     '* ** ** ** ** ** ** ** ** *',
#     '***************************',
#     '*********         *********',
#     '* ** ** *         * ** ** *',
#     '*********         *********',
#     '***   ***         ***   ***',
#     '* *   * *         * *   * *',
#     '***   ***         ***   ***',
#     '*********         *********',
#     '* ** ** *         * ** ** *',
#     '*********         *********',
#     '***************************',
#     '* ** ** ** ** ** ** ** ** *',
#     '***************************',
#     '***   ******   ******   ***',
#     '* *   * ** *   * ** *   * *',
#     '***   ******   ******   ***',
#     '***************************',
#     '* ** ** ** ** ** ** ** ** *',
#     '***************************'
# ]
#
# [
#     '*********',
#     '* ** ** *',
#     '*********',
#     '***   ***',
#     '* *   * *',
#     '***   ***',
#     '*********',
#     '* ** ** *',
#     '*********'
# ]


n = int(input())


def solution(n):
    if n == 3:
        return ["***", "* *", "***"]

    else:
        matrix = solution(n // 3)
        new_matrix = []
        for i in range(3):
            for j in range(len(matrix)):
                if i == 1:
                    new_matrix.append(matrix[j] + " " * len(matrix) + matrix[j])
                else:
                    new_matrix.append(matrix[j] * 3)
        return new_matrix


output = solution(n)

for ele in output:
    print(ele)
