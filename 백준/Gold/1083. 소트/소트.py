n = int(input())
lst = list(map(int, input().split(' ')))
s = int(input())


def solution(n, lst, s):
    for i in range(n):

        if s > 0:
            max_num = lst[i]
            idx = i
            for j in range(i, i + s + 1):
                if j < n and max_num < lst[j]:
                    max_num = lst[j]
                    idx = j
            if idx != i:
                max_num = lst.pop(idx)
                lst.insert(i, max_num)
                s -= idx - i
        else:
            break

    return ' '.join(map(str, lst))


print(solution(n, lst, s))
