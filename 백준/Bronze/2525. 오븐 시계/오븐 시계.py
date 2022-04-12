a, b = map(int, input().split(' '))
c = int(input())

시간 = c // 60
분 = c % 60

a += 시간
b += 분

if b >= 60:
    a += 1
    b -= 60

if a >= 24:
    a -= 24

print(a, b)