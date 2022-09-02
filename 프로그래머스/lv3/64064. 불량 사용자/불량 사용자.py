def solution(user_id, banned_id):
    check = [0] * (1 << (len(user_id) + 1))
    answer = 0
    lst = []

    for banned in banned_id:
        temp = []
        for user in user_id:
            if len(banned) != len(user):
                continue
            else:
                broke = False
                for i in range(len(banned)):
                    if banned[i] != "*" and banned[i] != user[i]:
                        broke = True
                        break
                if not broke:
                    temp.append(user)
        lst.append(temp)

    comb = [0]

    for i in range(len(lst)):
        temp = []
        while comb:
            pop = comb.pop(0)
            for j in range(len(lst[i])):
                if not pop & 1 << user_id.index(lst[i][j]):
                    temp.append(pop | 1 << user_id.index(lst[i][j]))
        comb = list(set(temp))
    return len(set(comb))


'''
frodo, fradi
frodo, crodo
frodo, fradi, crodo, abc123
frodoc

frodo, crodo
frodo, crodo
abc123, 


'''

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))
