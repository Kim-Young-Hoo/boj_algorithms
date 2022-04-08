import sys

n = int(input())


def solution(n):
    if n <= 10:
        return n

    if n > 1022:
        return -1

    lst = list(range(0, 10))

    cnt = 10

    while True:

        sub_list = []

        for i in range(0, 10):
            for ele in lst:
                if int(str(ele)[0]) < i:
                    sub_list.append(int(str(i) + str(ele)))
                    cnt += 1

                    if cnt - 1 == n:
                        return sub_list[-1]

                else:
                    break
        lst = sub_list


print(solution(n))
