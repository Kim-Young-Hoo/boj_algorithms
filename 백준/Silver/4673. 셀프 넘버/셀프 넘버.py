def d(num):

    result = num + sum(list(map(int, [list(str(num))[i] for i in range(len(list(str(num))))])))
    return result

arr = list(range(10001))

for i in range(10001):
    if i <= 10000:
        if d(i) in arr:
            arr.remove(d(i))


for ele in arr:
    print(ele)

