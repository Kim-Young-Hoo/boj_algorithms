"""
0: 6
1: 2
2: 5
3: 5
4: 4
5: 5
6: 6
7: 3
8: 7
9: 6


최대 : 자리수가 커야됨 == 1을 많이 사용해야됨 -> 더 사용할 수 없을 때 맨 앞자리를 최대한 큰 수로
남은 게 2일 때 1
남은 게 3일 때 7
남은 게 4일 때는 11
남은 게 5일 때는 71
남은 게 6일 때는 111
7일 때는 711
8일 때 1111
9일 때 7111
so on...

최소 : 자리수가 작아야 됨 == 8을 최대한 많이 사용해야됨
2일 때 1
3일 때 7
4일 때 4
5일 때 2
6일 때 6
7일 때 8
8일 때 10
9일 때 18
10일 때 22
11일 때 20
12일 때
15일 때 108
"""

t = int(input())

min_dict = {2: 1, 3: 7, 4: 4, 5: 2, 6: 0, 7: 8}

for i in range(8, 101):
    min_dict[i] = float("inf")
    for j in range(2, (i - 1) // 2 + 2):

        a = str(min_dict[i - j]) + str(min_dict[j])
        if a[0] == "0":
            a = "6" + str(min_dict[j])
        b = str(min_dict[j]) + str(min_dict[i - j])
        if b[0] == "0":
            b =  "6" + str(min_dict[i - j])

        min_dict[i] = min(min_dict[i], min(int(a), int(b)))



def get_min(n):
    if n == 6:
        return 6
    return min_dict[n]


def get_max(n):
    if n % 2 == 0:
        return int("1" * (n // 2))
    else:
        return int("7" + "1" * (n // 2 - 1))


def solution(n):
    min_val = get_min(n)
    max_val = get_max(n)
    return min_val, max_val


for _ in range(t):
    n = int(input())
    print(*solution(n))
