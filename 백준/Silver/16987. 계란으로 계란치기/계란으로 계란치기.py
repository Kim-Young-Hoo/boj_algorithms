n = int(input())

lst = []
weight = []
for _ in range(n):
    a, b = list(map(int, input().split(' ')))
    lst.append(a)
    weight.append(b)

max_cnt = 0


def solution(index, lst):
    global max_cnt

    if index == len(lst):
        max_cnt = max(max_cnt, len([ele for ele in lst if ele <= 0]))
        return

    if lst[index] <= 0:
        solution(index + 1, lst)

    for i in range(len(lst)):

        if index == i:
            continue

        if lst[i] > 0 and lst[index] > 0:
            original = [lst[index], lst[i]]

            lst[index] -= weight[i]
            lst[i] -= weight[index]

            solution(index + 1, lst)

            lst[index] = original[0]
            lst[i] = original[1]

    max_cnt = max(max_cnt, len([ele for ele in lst if ele <= 0]))


solution(0, lst)
print(max_cnt)
