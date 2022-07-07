n = int(input())
lst = list(map(int, input().split(' ')))
lst = sorted(lst)
m = int(input())
prob = list(map(int, input().split(' ')))


dic = {}
for i in range(n):
    if lst[i] in dic.keys():
        dic[lst[i]] += 1
    else:
        dic[lst[i]] = 1


answer = []

for i in range(m):
    if prob[i] in dic.keys():
        answer.append(dic[prob[i]])
    else:
        answer.append(0)


print(" ".join(map(str, answer)))
