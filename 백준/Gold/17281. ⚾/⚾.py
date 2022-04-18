from itertools import permutations
from collections import deque

n = int(input())
innings = []

for _ in range(n):
    innings.append(list(map(int, input().split(' '))))


def solution(n, innings):
    perm = list(permutations([1, 2, 3, 4, 5, 6, 7, 8], 8))

    max_score = 0

    for p in perm:
        p = list(p)
        p.insert(3, 0)

        current_out = 0
        base1, base2, base3 = 0, 0, 0
        current_idx = 0
        current_score = 0

        for inning in innings:
            inning = [inning[i] for i in p]

            while current_out < 3:
                if inning[current_idx] == 1:
                    if base3 == 1:
                        current_score += 1
                    base3, base2 = base2, base1
                    base1 = 1

                elif inning[current_idx] == 2:
                    if base3 == 1:
                        current_score += 1
                    if base2 == 1:
                        current_score += 1

                    base3 = base1
                    base2 = 1
                    base1 = 0
                elif inning[current_idx] == 3:
                    if base3 == 1:
                        current_score += 1
                    if base2 == 1:
                        current_score += 1
                    if base1 == 1:
                        current_score += 1

                    base3 = 1
                    base2 = 0
                    base1 = 0
                elif inning[current_idx] == 4:
                    current_score += base1 + base2 + base3 + 1
                    base1, base2, base3 = 0, 0, 0
                else:
                    current_out += 1

                if current_idx < 8:
                    current_idx += 1
                else:
                    current_idx = 0

            current_out = 0
            base1, base2, base3 = 0, 0, 0

        max_score = max(max_score, current_score)

    return max_score


print(solution(n, innings))