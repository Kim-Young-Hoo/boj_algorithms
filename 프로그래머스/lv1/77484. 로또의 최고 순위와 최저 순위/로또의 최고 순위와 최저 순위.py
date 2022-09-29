from itertools import combinations


def solution(lottos, win_nums):
    answer = [0, float("inf")]

    win_nums = set(win_nums)

    zero_cnt = 0
    matches = 0
    nums = list(range(1, 46))

    while lottos:
        pop = lottos.pop(0)
        if pop == 0:
            zero_cnt += 1
        else:
            if pop in win_nums:
                matches += 1



    for comb in combinations(nums, zero_cnt):
        num_match = 0

        for ele in comb:
            if ele in win_nums:
                num_match += 1

        answer[0] = max(answer[0], num_match + matches)
        answer[1] = min(answer[1], num_match + matches)

    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    return [dic[answer[0]], dic[answer[1]]]


