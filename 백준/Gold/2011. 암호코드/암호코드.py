import sys

lst = list(input())

dp = [0] * len(lst)
dp[0] = 1

if int(lst[0]) == 0:
    print(0)
    sys.exit()

if len(lst) == 1:
    print(1)
    sys.exit()
    
if int(lst[1]) == 0 and int(lst[0] + lst[1]) not in [10, 20]:
    print(0)
    sys.exit()

if 26 >= int(lst[0] + lst[1]) > 10 and int(lst[0] + lst[1]) != 20:
    dp[1] = 2
else:
    dp[1] = 1

for i in range(2, len(lst)):
    if int(lst[i]) == 0:
        if int(lst[i - 1] + lst[i]) not in [10, 20]:
            print(0)
            sys.exit()
        dp[i] = dp[i - 2] % 1000000

    elif 26 >= int(lst[i - 1] + lst[i]) > 10 and int(lst[i - 1] + lst[i]) != 20:
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000

    else:
        dp[i] = dp[i - 1] % 1000000

print(dp[-1])
