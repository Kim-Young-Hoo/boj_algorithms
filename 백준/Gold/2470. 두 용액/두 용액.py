n = int(input())
lst = list(map(int, input().split(' ')))


def solution(n, lst):
    lst = sorted(lst)
    left_pointer = 0
    right_pointer = n - 1

    min_val = float("inf")
    min_left = None
    min_right = None

    while right_pointer != left_pointer:

        two_sum = abs(lst[left_pointer] + lst[right_pointer])

        if two_sum < min_val:
            min_val = two_sum
            min_left = left_pointer
            min_right = right_pointer

        if abs(lst[left_pointer + 1] + lst[right_pointer]) > abs(lst[left_pointer] + lst[right_pointer - 1]):
            right_pointer -= 1
        else:
            left_pointer += 1

    return lst[min_left], lst[min_right]


left, right = solution(n, lst)
print(left, right)
