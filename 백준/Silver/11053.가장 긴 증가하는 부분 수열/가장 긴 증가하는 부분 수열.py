n = int(input())

a = list(map(int,input().split(' ')))

dp = [0] * len(a)
dp[0] = 1

for i in range(len(dp)):
    max_dp = 0
    
    for j in range(0,i,1):
        if a[j] < a[i] and max_dp < dp[j]:      
            max_dp = dp[j]
    
    dp[i] = max_dp + 1
    
print(max(dp))