import pprint
import sys

r, c = map(int, input().split(' '))

matrix = []
for _ in range(r):
    matrix.append(list(map(int, list(input()))))

dp = [[[0, 0] for _ in range(c)] for _ in range(r)]

max_dia = 0
for i in range(c):
    for j in range(r):
        if matrix[j][i] == 1:
            dp[j][i][0] = 1
            dp[j][i][1] = 1
            max_dia = 1

if max_dia == 0:
    print(0)
    sys.exit()


for i in range(1, r):
    for j in range(c):
        if matrix[i][j] == 1:
            if 0 <= j + 1 < c:
                dp[i][j][1] += dp[i - 1][j + 1][1]
            if 0 <= j - 1 < c:
                dp[i][j][0] += dp[i - 1][j - 1][0]

# pprint.pprint(dp)

for i in range(r):
    for j in range(c):
        min_branch = min(dp[i][j])
        if min_branch >= 2:
            while min_branch > 1:

                left = False
                right = False

                if 0 <= i - (min_branch - 1) < r and 0 <= j - (min_branch - 1) < c:
                    if dp[i - (min_branch - 1)][j - (min_branch - 1)][1] >= min_branch:
                        left = True

                if 0 <= i - (min_branch - 1) < r and 0 <= j + (min_branch - 1) < c:
                    if dp[i - (min_branch - 1)][j + (min_branch - 1)][0] >= min_branch:
                        right = True

                if left and right:
                    max_dia = max(max_dia, min_branch)
                    break
                else:
                    min_branch -= 1

print(max_dia)