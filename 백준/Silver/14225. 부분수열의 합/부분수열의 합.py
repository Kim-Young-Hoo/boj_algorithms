import sys

n = int(input())
s = list(map(int, input().split(' ')))

s = sorted(s)

def solution(n, s):
    temp_lst = [0]

    for i in range(n):
        temp_lst_length = len(temp_lst)
        for j in range(temp_lst_length):
            new_num = temp_lst[j] + s[i]
            if new_num > temp_lst[-1] + 1:
                print(temp_lst[-1] + 1)
                sys.exit()
            else:
                temp_lst.append(new_num)
    print(temp_lst[-1] + 1)


solution(n, s)