import bisect
def binary_search(arr,x):
    i = bisect.bisect_left(arr,x)
    return i < len(arr) and arr[i]==x
n=int(input())
arr = list(map(int,input().split()))
arr.sort()
m=int(input())
check=list(map(int,input().split()))
for i in range(m):
    if binary_search(arr,check[i]):
        print(1)
    else:
        print(0)
