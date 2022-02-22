"""
40 30 30 50 60

첫 for문
4(5-1)번 돈다
돌면서 1:2, 2:3, 3:4, 4:5 (i:i+1) 를 슬라이싱한다
dp[1][2] ... dp[4][5] 에다가 저장함

두번째 for문
3(5-2)번 돈다
돌면서 1:3, 2:4, 3:5 (i:i+2) 를 슬라이싱한다.
dp[1][3]의 경우 min(dp[1][2] + chapter[3], min[2][3] + chapter[1]을 dp[1][3]에 저장

"""




lst = []


def sol(chapter):

    # cn부터 cm까지 최소 비용 저장하는 dp
    dp = [[None] * len(chapter) for _ in range(len(chapter))]

    for i in range(len(chapter)-1):
        dp[i][i+1] = chapter[i] + chapter[i+1]

    for i in reversed(range(len(chapter)-2)):
        sub_list_length = len(chapter) - i
        for j in range(len(chapter)-sub_list_length+1):
            sub_list = chapter[j:j+sub_list_length]
            for k in range(2):
                dp[j][j+sub_list_length-1] = min(chapter[j] + dp[j+1][j+sub_list_length-1], chapter[j+sub_list_length-1] + dp[j][j+sub_list_length-2])
    return dp






# t = int(input())
# for i in range(t):
#     k = int(input())
#     chapter = list(map(int, input().split(' ')))
#

chapter = list(map(int, "40 30 30 50".split(' ')))
print(sol(chapter=chapter))