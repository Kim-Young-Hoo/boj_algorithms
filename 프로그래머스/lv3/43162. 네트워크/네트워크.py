from collections import deque



def solution(n, computers):
    answer = 0
    check = [0] * n

    for i in range(n):
        if not check[i]:
            check = dfs(i, n, computers, check)
            answer += 1
    print(check)
    return answer


def dfs(start_node, n, computers, check):
    stack = deque([start_node])
    while stack:
        pop = stack.pop()
        check[pop] = 1

        for i in range(n):
            if computers[pop][i] and not check[i]:
                stack.append(i)
    return check
