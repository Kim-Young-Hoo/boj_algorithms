import heapq


def solution(alp, cop, problems):
    max_alp = max([ele[0] for ele in problems])
    max_cop = max([ele[1] for ele in problems])

    problems.insert(0, [0, 0, 1, 0, 1])
    problems.insert(0, [0, 0, 0, 1, 1])
    queue = [(0, alp, cop)]

    dp = [[float("inf")] * 1000 for _ in range(1000)]

    while queue:
        dist, current_alp, current_cop = heapq.heappop(queue)
        if current_alp >= max_alp and current_cop >= max_cop:
            continue
        for problem in problems:

            if problem[0] > current_alp:
                continue
            if problem[1] > current_cop:
                continue

            next_alp = min(current_alp + problem[2], max_alp)
            next_cop = min(current_cop + problem[3], max_cop)
            next_dist = dist + problem[4]

            if 0 <= next_alp < 1000 and 0 <= next_cop < 1000:
                if dp[next_alp][next_cop] > next_dist:
                    heapq.heappush(queue, (next_dist, next_alp, next_cop))
                    dp[next_alp][next_cop] = next_dist
    return dp[max_alp][max_cop]


alp = 0
cop = 0
problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]  # 알고력, 코딩력, 증가하는 알고력, 증가하는 코딩력, 드는 시간

print(solution(alp, cop, problems))
