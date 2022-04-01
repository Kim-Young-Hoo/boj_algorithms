r1, c1, r2, c2 = list(map(int, input().split(' ')))

max_length = max(abs(r1), abs(r2), abs(c1), abs(c2)) * 2 + 1

matrix = [[0] * (c2 - c1 + 1) for _ in range(r2 - r1 + 1)]

number = 1

i = max_length // 2
j = max_length // 2

r1, c1, r2, c2 = i + r1, j + c1, i + r2, j + c2

lst = []

center_point = [i, j]

if r1 <= i <= r2 and c1 <= j <= c2:
    lst.append([number, i, j])

upper_right = [i - 1, j + 1]
upper_left = [i - 1, j - 1]
down_left = [i + 1, j - 1]
down_right = [i + 1, j + 1]

number += 1
j += 1

if r1 <= i <= r2 and c1 <= j <= c2:
    lst.append([number, i, j])

broke = False

while i <= max_length and j <= max_length:

    if broke:
        break

    # 위로 올라가
    while [i, j] != upper_right:
        i -= 1
        number += 1

        if r1 <= i <= r2 and c1 <= j <= c2:
            lst.append([number, i, j])

            if len(lst) == (c2 - c1 + 1) * (r2 - r1 + 1):
                broke = True
                break

    upper_right = [i - 1, j + 1]

    if broke:
        break

    # 왼쪽으로 가
    while [i, j] != upper_left:
        j -= 1
        number += 1
        if r1 <= i <= r2 and c1 <= j <= c2:
            lst.append([number, i, j])
            if len(lst) == (c2 - c1 + 1) * (r2 - r1 + 1):
                broke = True

                break

    upper_left = [i - 1, j - 1]

    if broke:
        break

    # 아래로 가
    while [i, j] != down_left:
        i += 1
        number += 1
        if r1 <= i <= r2 and c1 <= j <= c2:
            lst.append([number, i, j])
            if len(lst) == (c2 - c1 + 1) * (r2 - r1 + 1):
                broke = True

                break

    down_left = [i + 1, j - 1]

    if broke:
        break

    while [i, j] != down_right:
        j += 1
        number += 1
        if r1 <= i <= r2 and c1 <= j <= c2:
            lst.append([number, i, j])
            if len(lst) == (c2 - c1 + 1) * (r2 - r1 + 1):
                broke = True

                break

    down_right = [i + 1, j + 1]

    number += 1
    j += 1

    if broke:
        break

    if r1 <= i <= r2 and c1 <= j <= c2:
        lst.append([number, i, j])
        if len(lst) == (c2 - c1 + 1) * (r2 - r1 + 1):
            broke = True

            break

lst = sorted(lst, key=lambda x: x[2])
lst = sorted(lst, key=lambda x: x[1])

string_max_length = 0


idx = 0
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        string_max_length = max(string_max_length, len(str(lst[idx][0])))
        idx += 1


idx = 0
for i in range(r2 - r1 + 1):
    for j in range(c2 - c1 + 1):
        matrix[i][j] = '{num:{width}d}'.format(num=lst[idx][0], width=string_max_length)
        idx += 1

for ele in matrix:
    print(' '.join(list(map(str, ele))))
