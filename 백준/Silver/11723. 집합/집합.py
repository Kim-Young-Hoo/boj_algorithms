import sys

m = int(input())

s = [False] * 20


def solution(command):
    global s

    if command[0] == "add":
        s[int(command[1]) - 1] = True

    elif command[0] == "remove":
        s[int(command[1]) - 1] = False

    elif command[0] == "check":
        print(int(s[int(command[1]) - 1]))

    elif command[0] == "toggle":
        s[int(command[1]) - 1] = not s[int(command[1]) - 1]

    elif command[0] == "all":
        s = [True] * 20

    elif command[0] == "empty":
        s = [False] * 20


for _ in range(m):
    command = list(sys.stdin.readline().split())
    solution(command)
