"""
자기 이전꺼를 마셨을 때 : max(lst[i] + lst[i-1] + dp[:i-2])
자기 이전꺼를 안마셨을 때 : max(lst[i] + dp[:i])
"""


n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))


def sol(lst):

    if len(lst) == 1:
        return lst[0]

    if len(lst) == 2:
        return lst[0] + lst[1]


    dp = [lst[0], lst[0]+lst[1], max(lst[0]+lst[2], lst[1]+lst[2])]

    for i in range(3, len(lst)):
        a = lst[i] + lst[i-1] + max(dp[:i-2])
        b = lst[i] + max(dp[:i-1])
        dp.append(max(a, b))


    return max(dp)

print(sol(lst))

