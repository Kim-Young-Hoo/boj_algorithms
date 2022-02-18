n = int(input())


def sol(n):

    current_count = 1
    current_num = 666

    while n != current_count:
        current_num += 1
        if "666" in str(current_num):
            current_count += 1
    return current_num

print(sol(n))