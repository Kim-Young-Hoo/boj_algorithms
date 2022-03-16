n = int(input())

lst = []
for i in range(n):
    lst.append(int(input()))


def sol(lst):
    stack = []
    res = []
    i = 1
    while lst:
        pop = lst.pop(0)
        while True:
            if stack and stack[-1] == pop:
                res.append("-")
                stack.pop()
                break
            else:
                if i > pop:
                    return ["NO"]
                else:
                    stack.append(i)
                    res.append("+")
                    i += 1
    return res

res = sol(lst)
for ele in res:
    print(ele)