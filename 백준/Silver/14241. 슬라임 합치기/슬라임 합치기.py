n = int(input())
lst = list(map(int, input().split(' ')))



def sol(n, lst):


    slime = lst[0] + lst[1]
    score = lst[0] * lst[1]

    for i in range(2, len(lst)):
        score = score + slime*lst[i]
        slime += lst[i]

    return score

print(sol(n, lst))
