# print(ord("a"))
# print(ord("z"))
import sys

s = input()
q = int(input())

if len(s) == 0:
    print(0)
    sys.exit()


dp = [[0] * len(s) for _ in range(122 - 97 + 1)]
dp[ord(s[0]) - 97][0] = 1


for i in range(1, len(s)):

    for j in range(122 - 97 + 1):
        dp[j][i] = dp[j][i - 1]

    dp[ord(s[i]) - 97][i] = dp[ord(s[i]) - 97][i - 1] + 1


for i in range(q):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)

    if l == 0:
        sys.stdout.write(str(dp[ord(a) - 97][r]) + "\n")
    else:
        sys.stdout.write(str(dp[ord(a) - 97][r] - dp[ord(a) - 97][l - 1]) + "\n")
