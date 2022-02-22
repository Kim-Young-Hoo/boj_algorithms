"""
최종 연산 횟수는 무조건 k-1회

"""



lst = []


def sol(chapter):

    # cn부터 cm까지 최소 비용 저장하는 dp
    dp = [[10001] * len(chapter) for _ in range(len(chapter))]

    for i in range(len(chapter)-1):
        dp[i][i+1] = chapter[i] + chapter[i+1]

    for i in range(len(chapter)):
        for j in range(i, len(chapter)):
            dp[i][j] = min()






# t = int(input())
# for i in range(t):
#     k = int(input())
#     chapter = list(map(int, input().split(' ')))
#

# chapter = list("1 21 3 4 5 35 5 4 3 5 98 21 14 17 32".split(' '))
sol(chapter=chapter)
print(lst)