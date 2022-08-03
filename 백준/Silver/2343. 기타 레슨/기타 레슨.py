n, m = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))


def check(mid):
    global m

    group_cnt = 0
    current_group_size = 0
    for i in range(len(lst)):
        if mid < lst[i]:
            return False

        if current_group_size + lst[i] < mid:
            current_group_size += lst[i]
        elif current_group_size + lst[i] == mid:
            current_group_size = 0
            group_cnt += 1
        else:
            current_group_size = lst[i]
            group_cnt += 1
    if current_group_size > 0:
        group_cnt += 1

    return group_cnt <= m


def my_solution(lst):
    end = 100000 * 10000
    start = 0

    while start <= end:
        mid = (end + start) // 2

        if check(mid):
            end = mid - 1
        else:
            start = mid + 1

    return end


print(my_solution(lst) + 1)
