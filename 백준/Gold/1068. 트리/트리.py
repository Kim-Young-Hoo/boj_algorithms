n = int(input())
lst = list(map(int, input().split(' ')))
delete_node = int(input())


def solution(n, lst, delete_node):
    leaf_cnt_lst = [0] * n

    if lst[delete_node] == -1:
        return 0

    lst[delete_node] = float("inf")

    for i in range(n):
        if lst[i] == -1:
            continue
        else:
            current_node = i
            path = []
            while lst[current_node] not in [-1, float("inf")]:
                path.append(current_node)
                leaf_cnt_lst[lst[current_node]] += 1
                current_node = lst[current_node]
            if lst[current_node] == -1:
                continue
            else:
                for node in path:
                    lst[node] = float("inf")

    cnt = 0
    for i in range(n):
        if lst[i] != float("inf") and leaf_cnt_lst[i] == 0:
            cnt += 1

    return cnt


print(solution(n, lst, delete_node))
