# your code goes here

# your code goes here

# your code goes here


# your code goes here

# your code goes here


s = str(input())
# s = list(s.split('-'))


#s="55-50+40"
arr = list(s.split('-'))

result = 0


def calc(arr):
    
    result = 0
    for ele in arr:
        result += int(ele)
       
    return result
        



for i in range(len(arr)):
    arr2 = arr[i].split('+')
    arr2 = [int(x) for x in arr2]
    now = calc(arr2)
    
    if i == 0 and now > 0:
        now = now * -1
    
    result -= now

print(result)