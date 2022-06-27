n, s = map(int, input().split(' '))
lst = sorted(list(map(int, input().split(' '))))

cnt = 0

# print(len(lst))


def solution(n, s, lst, current_idx, current_sum):
    global cnt

    if current_sum == s:
        cnt += 1
    if current_sum > s >= 0:
        return

    for i in range(current_idx + 1, len(lst)):
        solution(n, s, lst, i, current_sum + lst[i])


for idx in range(len(lst)):
    solution(n, s, lst, idx, current_sum=lst[idx])
print(cnt)
