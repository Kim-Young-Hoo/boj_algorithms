def is_prime(num):
    if (num <= 1):
        return False

    i = 2
    while i * i <= num:
        if num % i == 0:
            return False

        i += 1
    return True


n = int(input())

def soinsu(n):
    

    
    
    i = 2
    
    while n != 1:
        
        if n == 1:
            return None
        
        
        if n % i == 0:
            n /= i
            print(i)
            
        else:
            i += 1

soinsu(n)

