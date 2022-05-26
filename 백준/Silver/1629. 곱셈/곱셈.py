a,b,c = map(int, input().split(' '))

def double(a, b):
        
    if b == 0:
        return 1

    elif b == 1:
        return a
    
    elif b % 2 > 0:
        return double(a, b-1) * a
    
    h = double(a, b//2)
    h %= c
    return h ** 2 % c
        
print(double(a, b) % c)  