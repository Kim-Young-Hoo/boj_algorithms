
n = int(input())

x_lst = []
y_lst = []

for _ in range(n):
    x, y = map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)

x_lst.append(x_lst[0])
y_lst.append(y_lst[0])

sum_a = 0
sum_b = 0

for i in range(n):
    sum_a += x_lst[i] * y_lst[i + 1]
for i in range(n):
    sum_b += y_lst[i] * x_lst[i + 1]

res = sum_a - sum_b
res /= 2
res = abs(res)
res = round(res, 2)

print(res)
