from collections import deque

n, k = list(map(int, input().split(' ')))


def sol(n, k):
    if n == k:
        return 0

    count = [0 for _ in range(100001)]
    need_visit = deque([n])

    while need_visit:
        node = need_visit.popleft()

        if node == k:
            return count[node]

        for ele in (node - 1, node + 1, node * 2):
            if 0 <= ele <= 100000 and count[ele] == 0:
                need_visit.append(ele)
                count[ele] = count[node] + 1


print(sol(n, k))
