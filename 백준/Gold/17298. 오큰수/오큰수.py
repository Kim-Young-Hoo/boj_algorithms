def oken(arr):
    
    result = []
    stack = []
    
    max_val = -1
    
    for i in range(len(arr)):
        current = arr[i]
        
        stack = arr[i+1:]
        
        for k in range(len(stack)):
            pops = stack.pop()
            
            if pops > current:
                max_val = pops
                
        result.append(str(max_val))
        max_val = -1
    
    return ' '.join(result)
    


def oken2(arr):
    
    stack = []
    result = [-1] * len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        while(len(stack) != 0 and stack[-1] <= arr[i]):
            stack.pop()
        
        if len(stack) == 0:
            result[i] = -1

        else:
            result[i] = stack[-1]

        stack.append(arr[i])
            
    return ' '.join([str(x) for x in  result])
    
# arr = np.random.random(1000) * 10
# arr = [int(x) for x in arr]
    
n = int(input())
arr = list(map(int,input().split(' ')))

# arr = [3,5,2,7]

print(oken2(arr))
    
    
    
    
    
    