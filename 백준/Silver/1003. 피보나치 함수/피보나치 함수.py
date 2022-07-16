"""
fibo(0) = 1 0
fibo(1) = 0 1
fibo(2) = fibo(0) + fibo(1) = 1 1
fibo(3) = fibo(1) + fibo(2) = 0 1 + 1 1 = 1 2
fobi(4) = fibo(2) + fibo(3) = 1 1 + 1 2 = 2 3
"""


def sol(n):
    res = [[1, 0], [0, 1]]

    if n == 0:
        print("1 0")
        return
    if n == 1:
        print("0 1")
        return

    for i in range(n-1):
        new_ele = [0, 0]
        new_ele[0] = res[-2][0] + res[-1][0]
        new_ele[1] = res[-2][1] + res[-1][1]
        res.append(new_ele)

    print(res[-1][0], res[-1][1])
    return



t = int(input())

for i in range(t):
    sol(int(input()))



