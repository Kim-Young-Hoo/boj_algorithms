n, m = map(int, input().split(' '))
truth = list(map(int, input().split(' ')))[1:]

dictionary = {
    ele: 0 for ele in range(1, n + 1)
}

for t in truth:
    dictionary[t] = -1


parties = []
for _ in range(m):
    lst = list(map(int, input().split(' ')))[1:]
    parties.append(lst)

    is_possible = True
    for ele in lst:
        if dictionary[ele] == -1:
            is_possible = False
            break


while truth:
    pop = truth.pop(0)

    for party in parties:
        if pop in party:
            for ele in party:
                if dictionary[ele] != -1:
                    dictionary[ele] = -1
                    truth.append(ele)



cnt = 0
for party in parties:
    is_possible = True
    for ele in party:
        if dictionary[ele] == -1:
            is_possible = False
            break
    if is_possible:
        cnt += 1
print(cnt)