n = int(input())
lst = list(map(int, input().split(' ')))

max_val = 0


def solution(n, lst, current_sum):
    global max_val

    if len(lst) == 2:
        max_val = max(max_val, current_sum)
        return

    for i in range(1, len(lst) - 1):
        new_lst = lst[:i] + lst[i + 1:]
        solution(n, new_lst, current_sum + lst[i - 1] * lst[i + 1])


solution(n, lst, 0)
print(max_val)
