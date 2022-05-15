"""
1. 높은 자리수에 있는 문자를 높은 숫자로
2. 같은 자리수에 있는 문자들 중 더 출현빈도가 많은 거를 높은 숫자로
"""


import heapq

n = int(input())

original_lst = []
lst = []
for _ in range(n):
    word = input()
    original_lst.append(word)
    lst.append(word.zfill(10))


def solution(n, lst):

    dictionary = {}

    current_num = 1000000000
    for i in range(10):
        for j in range(n):
            if lst[j][i] != "0":
                if lst[j][i] in dictionary.keys():
                    dictionary[lst[j][i]] += current_num
                else:
                    dictionary[lst[j][i]] = current_num
        current_num /= 10

    heap = []
    for key, val in dictionary.items():
        heapq.heappush(heap, (-val, key))

    dictionary = {}
    current_num = 9
    while heap:
        val, letter = heapq.heappop(heap)
        dictionary[letter] = current_num
        current_num -= 1

    cum_sum = 0
    for i in range(n):
        current_string = ""
        for j in range(len(original_lst[i])):
            current_string += str(dictionary[original_lst[i][j]])
        cum_sum += int(current_string)

    return cum_sum

print(solution(n, lst))

