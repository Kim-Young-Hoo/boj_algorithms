n = int(input())
lst = list(map(int, input().split(' ')))


def sol(lst):
    dic = {ele: 0 for ele in set(lst)}
    new_lst = sorted(list(set(lst)))
    for i in range(len(new_lst)):
        dic[new_lst[i]] = i
    res = []
    for ele in lst:
        res.append(dic[ele])

    return ' '.join(list(map(str, res)))

print(sol(lst))