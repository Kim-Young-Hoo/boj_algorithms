"""
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6

sort 하면
1 8 <- 고르면 다음엔 무조건 8번 초과부터 시작해야됨 (index i)
2 2
3 9
4 1
6 4
7 6
9 7 <- 여기로 오기 때문에 하나 추가 가능 근데 이 사이에는 전부 불가능 (index j)
10 10 <- 얘도 추가 가능


걍 정렬하고 B전봇대 부분증가수열 구하면 될거 같은데?


"""


n = int(input())

lst = []

for i in range(n):
    lst.append(list(map(int, input().split(' '))))


def inc_bitonic(lst):
    lst = sorted(lst, key=lambda x: x[0])
    b = [x[1] for x in lst]

    dp = [0] * len(b)
    dp[1] = 1

    for i in range(len(dp)):
        max_dp = 0

        for j in range(0, i, 1):
            if b[j] < b[i] and max_dp < dp[j]:
                max_dp = dp[j]

        dp[i] = max_dp + 1

    return len(dp) - max(dp)

print(inc_bitonic(lst))




