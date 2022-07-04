import sys

n = int(input())
a = list(map(int, list(input())))
b = list(map(int, list(input())))


def solution(state):
    global n

    index_zero_pushed = False
    min_cnt = float("inf")
    original_state = [ele for ele in state]

    for _ in range(2):
        cnt = 0

        if index_zero_pushed:
            cnt += 1
            state[0] = not state[0]
            state[1] = not state[1]

        for i in range(1, n):

            if state[i - 1] != b[i - 1]:
                state[i - 1] = not state[i - 1]
                state[i] = not state[i]
                if i < n - 1:
                    state[i + 1] = not state[i + 1]
                cnt += 1

        if state == b:
            min_cnt = min(min_cnt, cnt)

        index_zero_pushed = not index_zero_pushed
        state = original_state

    if min_cnt != float("inf"):
        return min_cnt

    return -1


print(solution(a))
