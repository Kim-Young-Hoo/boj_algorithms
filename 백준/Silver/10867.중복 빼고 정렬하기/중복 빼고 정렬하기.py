n = int(input())
lst = list(map(int, input().split(' ')))


def sol(n, lst):

    res = [lst[0], float('inf')]

    for i in range(n):
        if lst[i] in res:
            continue
        for j in range(len(res)):
            if res[j] > lst[i]:
                res.insert(j, lst[i])
                break

    return ' '.join(list(map(str, res[:-1])))

print(sol(n, lst))

