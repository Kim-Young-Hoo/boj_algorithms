n, s = map(int, input().split(' '))

lst = list(map(int, input().split(' ')))


def solution(n, s, lst):
    current_sum = lst[0]
    shortest = float("inf")
    right_pointer = 0
    left_pointer = 0
    while right_pointer >= left_pointer:
        if current_sum >= s:
            shortest = min(shortest, right_pointer - left_pointer + 1)

        if current_sum < s and right_pointer < n - 1:
            right_pointer += 1
            current_sum += lst[right_pointer]

        else:
            current_sum -= lst[left_pointer]
            left_pointer += 1

    if shortest < float("inf"):
        return shortest
    else:
        return 0


print(solution(n, s, lst))
