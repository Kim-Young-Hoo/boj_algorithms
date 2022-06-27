from itertools import permutations


k = int(input())
lst = list(map(str, input().split(' ')))

perm = permutations(range(0, 10), k + 1)

result = []

for p in perm:
    temp_nums = list(p)
    temp_lst = [ele for ele in lst]

    is_ok = True

    left_num = temp_nums.pop(0)
    while temp_nums:
        sign = temp_lst.pop(0)
        right_num = temp_nums.pop(0)

        if sign == "<":
            if left_num < right_num:
                pass
            else:
                is_ok = False
                break
        else:
            if left_num > right_num:
                pass
            else:
                is_ok = False
                break
        left_num = right_num

    if is_ok:
        result.append(''.join(map(str, p)))
        break

for p in reversed(list(perm)):
    temp_nums = list(p)
    temp_lst = [ele for ele in lst]

    is_ok = True

    left_num = temp_nums.pop(0)
    while temp_nums:
        sign = temp_lst.pop(0)
        right_num = temp_nums.pop(0)

        if sign == "<":
            if left_num < right_num:
                pass
            else:
                is_ok = False
                break
        else:
            if left_num > right_num:
                pass
            else:
                is_ok = False
                break
        left_num = right_num

    if is_ok:
        result.append(''.join(map(str, p)))
        break

print(result[-1])
print(result[0])
