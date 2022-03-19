def solution(N, stages):
    answer = []

    arrive = [0] * (N + 1)
    fail = [0] * (N + 1)

    for stage in stages:
        for i in range(stage):
            arrive[i] += 1
        fail[stage - 1] += 1

    for i in range(len(arrive) - 1):
        if arrive[i] > 0:
            answer.append(fail[i] / arrive[i])
        else:
            answer.append(0)

    answer = sorted(range(len(answer)), key=lambda k: answer[k], reverse=True)
    answer = [ele + 1 for ele in answer]

    return answer


# print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# print(solution(4, [4, 4, 4, 4, 4]))
# print(solution(3, [1, 1, 1]))
print(solution(5, [2, 1, 2, 4, 2, 4, 3, 3]))
