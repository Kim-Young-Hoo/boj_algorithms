from itertools import combinations

n, m = map(int, input().split(' '))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))


def solution(n, m, matrix):

    min_dist = float("inf")

    house_lst = []
    chick_lst = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:
                house_lst.append((i, j))
            elif matrix[i][j] == 2:
                chick_lst.append((i, j))

    chick_combination = list(combinations(chick_lst, m))

    for combi in chick_combination:

        dictionary = {h: float("inf") for h in house_lst}

        for chick in combi:
            for house in house_lst:
                current_sum = abs(chick[0] - house[0]) + abs(chick[1] - house[1])

                if current_sum < dictionary[house]:
                    dictionary[house] = current_sum

            min_dist = min(sum(dictionary.values()), min_dist)

    return min_dist


print(solution(n, m, matrix))
