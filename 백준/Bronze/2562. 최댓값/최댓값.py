arr = []
for i in range(9):
    arr.append(int(input()))
    
    
def sol(arr):
    max_ = max(arr)
    max_idx = None 
    
    for i, ele in enumerate(arr):
        if ele == max_:
            max_idx=i+1
            
    return max_, max_idx

max_, max_idx=sol(arr)

print(max_)
print(max_idx)