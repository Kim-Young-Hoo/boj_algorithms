from collections import deque

a, b, c = map(int, input().split(' '))

visited = [[0] * 1000 for _ in range(1000)]


def solution(a, b, c):
    is_possible = 0

    a, b, c = sorted([a, b, c])
    visited[a][b] = 1
    queue = deque([[a, b, c]])

    while queue:
        a, b, c = queue.popleft()

        if a == b == c:
            is_possible = 1
            break

        if a != b and a * 2 != b:
            a1, b1, c1 = sorted([a * 2, b - a, c])
            if not visited[a1][b1]:
                queue.append([a1, b1, c1])
                visited[a1][b1] = 1

        if a != c and a * 2 != c:
            a1, b1, c1 = sorted([a * 2, b, c - a])
            if not visited[a1][b1]:
                queue.append([a1, b1, c1])
                visited[a1][b1] = 1

        if b != c and b * 2 != c:
            a1, b1, c1 = sorted([a, b * 2, c - b])
            if not visited[a1][b1]:
                queue.append([a1, b1, c1])
                visited[a1][b1] = 1

    return is_possible


print(solution(a, b, c))
