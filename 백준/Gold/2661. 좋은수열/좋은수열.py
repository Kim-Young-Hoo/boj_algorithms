import sys

n = int(input())

string_list = []


def solution(n, current_string="1"):
    numbers = ["1", "2", "3"]


    splitter = 2
    is_possible = True
    while splitter <= n // 2:
        right = current_string[len(current_string) - splitter:len(current_string)]
        left = current_string[len(current_string) - 2 * splitter:len(current_string) - splitter]

        if left == right:
            is_possible = False
            break
        splitter += 1
    if not is_possible:
        return

    if len(current_string) == n:
        print(current_string)
        sys.exit()

    for number in numbers:
        if number != current_string[-1]:
            solution(n, current_string + number)


solution(n, "1")
print(string_list[0])