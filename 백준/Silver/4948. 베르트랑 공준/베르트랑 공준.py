import math



def solution(n):
    sieve = [True] * (2*n+1)

    m = round((2*n+1) ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:           # i가 소수인 경우
            for j in range(i+i, 2*n+1, i): # i이후 i의 배수들을 False 판정
                sieve[j] = False

    return sum([sieve[i] for i in range(n+1, 2*n+1) if sieve[i] == True])





while True:
    n = int(input())

    if n == 0:
        break
    else:
        print(solution(n))