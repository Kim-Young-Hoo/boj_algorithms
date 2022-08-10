def is_prime(num):
    if (num <= 1):
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False

        i += 1
    return True


def devide_2(n):

    a = n//2
    b = n//2

    while True:

        if (is_prime(a)) and (is_prime(b)):
            return a, b
        else:
            a -= 1
            b += 1


n = int(input())

for i in range(n):
    a, b = devide_2(int(input()))
    print(a, b)