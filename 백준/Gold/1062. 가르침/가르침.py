# strings = ["antarctica", "antahellotica", "antacartica"]
# bits = []
#
# for string in strings:
#     b = 0b0
#     for char in string:
#         b = b | (1 << ord(char) - 97)
#     bits.append(bin(b))
#
# print(bits)

from itertools import combinations

n, k = map(int, input().split(' '))

words = []
for _ in range(n):
    word = input()
    b = 0b0
    for char in word:
        b = b | (1 << ord(char) - 97)
    words.append(b)


def solution(n, k, words):
    if k < 5:
        return 0

    elif k == 26:
        return n

    alphabets = list("bdefghjklmopqrsuvwxyz")
    combs = combinations(alphabets, k - 5)

    max_cnt = 0

    for comb in combs:
        cnt = 0
        learn = 0b10000010000100000101
        for c in comb:
            learn = learn | 1 << ord(c) - 97

        for word in words:
            if learn & word == word:
                cnt += 1
        max_cnt = max(cnt, max_cnt)

    return max_cnt


print(solution(n, k, words))
