from collections import deque

t = int(input())


def solution(p, n, lst):
    r_count = 0
    pop_left_count = 0
    pop_right_count = 0

    for i in range(len(p)):
        if p[i] == "R":
            r_count = (r_count + 1) % 2
        else:
            if r_count == 1:
                pop_right_count += 1
            else:
                pop_left_count += 1

    if pop_left_count + pop_right_count > len(lst):
        return "error"

    for _ in range(pop_right_count):
        lst.pop()
    for _ in range(pop_left_count):
        lst.popleft()

    if r_count == 1:
        return "["+','.join(map(str, list(reversed(lst))))+"]"
    else:
        return "["+','.join(map(str, list(lst)))+"]"


for i in range(t):
    p = str(input())
    n = int(input())
    lst = deque(eval(str(input())))
    print(solution(p, n, lst))
