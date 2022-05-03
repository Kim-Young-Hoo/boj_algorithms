n = int(input())
arr = list(map(int,input().split(' ')))

arr.sort()

time = [0] * n

time[0] = arr[0]

for i in range(1, n):
    time[i] = (time[i-1] + arr[i])

    
print(sum(time))
    












