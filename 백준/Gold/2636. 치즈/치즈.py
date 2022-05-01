"""
1. 최초 순회는 (0,0)에서 무조건 0인 애들만 순회
2. 0->0으로 이동한 칸은 다시 안 가도록 visited에 True로 표기
3. 0->1로 이동하는 칸은 없어지는 칸임 next_queue에 담았다가 다음번 순회의 시작 queue로
4. queue pop 하면서 그 칸은 0으로 변경
"""
from collections import deque

n, m = map(int, input().split(' '))
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))


def solution(n, m, matrix):
    cnt = -1
    queue = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    next_queue = deque([])
    d = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    last = 0
    for ele in matrix:
        last+= ele.count(1)

    while queue:
        while queue:
            x, y = queue.popleft()
            matrix[x][y] = 0

            for dx, dy in d:
                new_x, new_y = dx + x, dy + y

                if 0 <= new_x < n and 0 <= new_y < m:
                    if matrix[new_x][new_y] == 1:
                        next_queue.append((new_x, new_y))
                    elif matrix[new_x][new_y] == 0 and visited[new_x][new_y] == False:
                        queue.append((new_x, new_y))
                        visited[new_x][new_y] = True
        if len(next_queue) > 0:
            queue = next_queue
            next_queue = deque([])
            cnt += 1

            last_cnt = 0
            for ele in matrix:
                last_cnt += ele.count(1)
            if last_cnt > 0:
                last = last_cnt

        else:
            break

    return cnt, last


cnt, last = solution(n, m, matrix)
print(cnt)
print(last)
