n = int(input())
cranes = list(map(int, input().split(' ')))
m = int(input())
boxes = list(map(int, input().split(' ')))
cranes = sorted(cranes, reverse=True)
boxes = sorted(boxes, reverse=True)


def solution(cranes, boxes):
    cnt = 0
    mask = [False] * len(boxes)
    crane_idx = [0] * len(cranes)


    if cranes[0] < boxes[0]:
        return -1

    while sum(mask) != len(mask):
        for i in range(len(cranes)):
            while crane_idx[i] < len(boxes):
                if cranes[i] >= boxes[crane_idx[i]] and not mask[crane_idx[i]]:
                    mask[crane_idx[i]] = True
                    break
                else:
                    crane_idx[i] += 1
        cnt += 1

    return cnt


print(solution(cranes, boxes))
