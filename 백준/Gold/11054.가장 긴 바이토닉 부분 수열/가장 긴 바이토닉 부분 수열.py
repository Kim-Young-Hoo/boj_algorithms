n = int(input())

a = list(map(int,input().split(' ')))

dp = [0] * len(a)

inc_dp = [0] * len(a)
inc_dp[0] = 1

dec_dp = [0] * len(a)

#증가하는 수열 

for i in range(len(inc_dp)):
    max_dp = 0

    for j in range(0,i,1):
        if a[j] < a[i] and max_dp < inc_dp[j]:      
            max_dp = inc_dp[j]
            
    inc_dp[i] = max_dp + 1

#i번째마다의 감소하는 수열


for k in range(len(dec_dp)):
    
    # k를 기준으로 뒷부분만 slicing
    
    temp_a = a[k:]
    temp_a = list(reversed(temp_a))
    
    temp_dec_dp = [0] * len(temp_a)

    #temp_a에 대해서 증가하는 부분 수열
    for i in range(len(temp_a)):
        max_dp = 0

        for j in range(0,i,1):
            if temp_a[j] < temp_a[i] and max_dp < temp_dec_dp[j]:      
                max_dp = temp_dec_dp[j]

        temp_dec_dp[i] = max_dp + 1
    
    dec_dp[k] = temp_dec_dp[-1]
    


for i in range(len(dp)):
    
    dp[i] = inc_dp[i] + dec_dp[i] - 1
    
print(max(dp))