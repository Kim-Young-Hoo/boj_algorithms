n = int(input())

for i in range(n):
    a, b = map(int, input().split(' '))

    importance = list(map(int, input().split(' ')))

    masking = [0] * a
    masking[b] = 1

    # print('masking : ', masking)
    # print('importance : ', importance)
    # print('max : ', max(importance))
    output = 0

    while True:

        if (importance[0] == max(importance)) and (masking[0] == 1):
            # print('first')
            output += 1
            break

        elif (importance[0] == max(importance)) and (masking[0] == 0):
            # print('second')
            importance.pop(0)

            masking.pop(0)

            output += 1

        else:
            # print('third')
            p = importance.pop(0)
            importance.append(p)

            p = masking.pop(0)
            masking.append(p)

        # print(importance)
        # print(masking)
    print(output)
