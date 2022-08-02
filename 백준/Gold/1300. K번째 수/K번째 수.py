n = int(input())
k = int(input())


def check(mid):
    global n, k
    return sum([min(mid // ele, n) for ele in range(1, n + 1)]) >= k


start = 1
end = k

while start <= end:
    mid = (start + end) // 2

    if check(mid):
        end = mid - 1
    else:
        start = mid + 1

print(start)
