from collections import deque

s = deque(list(input()))
bomb = input()

stack = deque([])

while s:
    pop = s.popleft()
    if pop != bomb[-1]:
        stack.append(pop)
    else:
        temp = ""
        for i in range(len(bomb) - 1):
            if stack:
                temp = stack.pop() + temp
            else:
                break
        temp = temp + pop

        if temp == bomb:
            continue
        else:
            for i in range(len(temp)):
                stack.append(temp[i])

if stack:
    print(''.join(stack))
else:
    print("FRULA")