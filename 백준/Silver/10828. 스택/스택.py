from collections import deque
import sys


n = int(input())
stack = deque([])


def solution(command):
    global stack
    if command[0] == "push":
        stack.append(command[1])
    elif command[0] == "pop":
        if len(stack) > 0:
            print(stack.pop())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(stack))
    elif command[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

for i in range(n):
    solution(list(sys.stdin.readline().split()))