n = int(input())
lst = list(map(int, input().split(' ')))
x = int(input())


def solution(n, x, lst):
    lst = sorted(lst)
    left_pointer = 0
    right_pointer = n - 1

    cnt = 0
    while right_pointer != left_pointer:
        two_sum = lst[left_pointer] + lst[right_pointer]
        if two_sum > x:
            right_pointer -= 1
        elif two_sum < x:
            left_pointer += 1
        else:
            cnt += 1
            left_pointer += 1

    return cnt


print(solution(n, x, lst))
