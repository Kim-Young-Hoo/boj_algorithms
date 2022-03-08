n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))





def sol(lst):

    max_arr = [0] * (len(lst))
    max_arr[0] = lst[0]
    if len(lst) > 1:
        max_arr[1] = max(lst[0]+lst[1], lst[1])
    if len(lst) > 2:
        max_arr[2] = max(lst[2]+lst[0], lst[1]+lst[2])

    for i in range(2, len(lst)):

        max_arr[i] = max(max_arr[i-3] + lst[i-1] + lst[i], max_arr[i-2] + lst[i])

    return max_arr[-1]

print(sol(lst))
