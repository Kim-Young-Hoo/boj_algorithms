n = int(input())
lst = list(map(int, input().split(' ')))


def solution(n, lst):
    max_cnt = 0

    for start_building in range(n):
        left_buildings = reversed([ele - lst[start_building] for ele in lst[:start_building]])
        right_buildings = [ele - lst[start_building] for ele in lst[start_building:]][1:]
        cnt = 0

        current_formula = float("-inf")
        for dist, height in enumerate(right_buildings):
            if current_formula == float("-inf") or height > (dist + 1) * current_formula:
                current_formula = height / (dist + 1)
                cnt += 1

        current_formula = float("-inf")
        for dist, height in enumerate(left_buildings):
            if current_formula == float("-inf") or height > (dist + 1) * current_formula:
                current_formula = height / (dist + 1)
                cnt += 1

        max_cnt = max(max_cnt, cnt)

    return max_cnt


print(solution(n, lst))
