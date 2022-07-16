n = int(input())

def sol(n):

    output = [1, 2]

    result = None

    for i in range(n-2):
        result = (output[0] + output[1])% 15746
        output[0] = output[1]% 15746
        output[1] = result% 15746

    if n == 1:
        return output[0]

    if n == 2:
        return output[1]

    else:
        return result

print(sol(n))
