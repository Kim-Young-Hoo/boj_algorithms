def func(n):
    len_n = len(n)
    target_num = "1" * len_n

    while True:
        if int(target_num) % int(n) == 0:
            return len(target_num)
        else:
            target_num += "1"


while True:
    try:
        n = input()
        print(func(n))
    except EOFError:
        break


