import sys

m = int(input())

s = 0
for _ in range(m):
    command = list(sys.stdin.readline().split())

    if command[0] == "add":
        s = s | (1 << int(command[1]) - 1)
    elif command[0] == "remove":
        s = s & ~(1 << int(command[1]) - 1)
    elif command[0] == "check":
        if s & (1 << int(command[1]) - 1):
            print(1)
        else:
            print(0)
    elif command[0] == "toggle":
        s = s ^ (1 << int(command[1]) - 1)
    elif command[0] == "all":
        s = 2 ** 20 - 1
    else:
        s = 0
