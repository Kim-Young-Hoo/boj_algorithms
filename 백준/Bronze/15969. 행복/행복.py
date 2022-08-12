n = int(input())
lst = list(map(int, input().split(' ')))

max_val = 0
min_val = float("inf")
for i in range(n):
    max_val = max(max_val, lst[i])
    min_val = min(min_val, lst[i])
    
print(max_val - min_val)