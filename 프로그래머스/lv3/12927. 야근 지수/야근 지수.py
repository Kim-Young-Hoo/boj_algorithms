from collections import deque


def solution(n, works):
    cnt = [0] * 500000

    for i in range(len(works)):
        cnt[works[i]] += 1
    works = deque(list(sorted(set(works))))

    while n > 0:
        max_val = works.pop()
        if max_val == 0:
            break

        if n >= cnt[max_val]:
            n -= cnt[max_val]
            if not cnt[max_val - 1]:
                works.append(max_val - 1)
            cnt[max_val - 1] += cnt[max_val]
            cnt[max_val] = 0
        else:
            cnt[max_val - 1] += n
            cnt[max_val] -= n
            n = 0

    return sum([(idx ** 2) * val for idx, val in enumerate(cnt)])


print(solution(3, [1, 1]))
