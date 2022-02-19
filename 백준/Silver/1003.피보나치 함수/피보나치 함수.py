def fibo(n):
    fibo_lst_1 = [1, 0, 0]
    fibo_lst_2 = [0,1,0]
    if n == 0:
        return 1, 0
    if n == 1:
        return 0, 1
    if n == 2:
        return 1, 1    
    else:
        for i in range(n-1):
            fibo_lst_1[2] = fibo_lst_1[0] + fibo_lst_1[1]
            fibo_lst_1[0] = fibo_lst_1[1]
            fibo_lst_1[1] = fibo_lst_1[2]
            fibo_lst_2[2] = fibo_lst_2[0] + fibo_lst_2[1]
            fibo_lst_2[0] = fibo_lst_2[1]
            fibo_lst_2[1] = fibo_lst_2[2]
        return fibo_lst_1[1], fibo_lst_2[2]

N = int(input())

for i in range(N):
    n = int(input())
        
    a = fibo(n)
    print(a[0], a[1])
