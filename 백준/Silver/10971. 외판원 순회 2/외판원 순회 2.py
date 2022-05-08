n = int(input())

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

min_sum = float("inf")


def solution(mask, start, last, cum_sum):
    global matrix
    global n
    global min_sum

    if cum_sum >= min_sum:
        return

    if mask.count(False) == 0 and matrix[last][start] > 0:
        min_sum = min(cum_sum + matrix[last][start], min_sum)
        return

    for i in range(n):
        if last != i and not mask[i] and matrix[last][i] > 0:
            new_mask = [ele for ele in mask]
            new_mask[i] = True
            solution(new_mask, start, i, cum_sum + matrix[last][i])


for i in range(n):
    mask = [False] * n
    mask[i] = True
    solution(mask, i, i, 0)

print(min_sum)
