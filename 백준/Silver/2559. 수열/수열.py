n, k = map(int, input().split(' '))
lst = list(map(int, input().split(' ')))
res = [float("-inf")] * n
res[0] = sum(lst[0:k])

for i in range(1, n - k + 1):
    res[i] = res[i - 1] - lst[i - 1] + lst[i + k - 1]

print(max(res))
