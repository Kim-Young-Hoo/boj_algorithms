n = int(input())

lst = []
for _ in range(n):
    lst.append(int(input()))


def sol(lst):

    dp1 = [lst[0], lst[0]+lst[1]] # 자기 이전꺼를 마셨을 때 dp
    dp2 = [lst[0], lst[1]] # 자기 이전꺼를 마시지 않았을 때 dp

    for i in range(2, len(lst)):
        if lst[i] == 0:
            dp1.append(dp1[i-1])
            dp2.append(dp2[i-1])

        dp1.append(dp2[i-1] + lst[i])
        dp2.append(dp1[i-2] + lst[i])

    # print([6, 10, 13, 9, 8, 1])
    print(dp1, dp2)

    return max(max(dp1), max(dp2))

print(sol(lst))

