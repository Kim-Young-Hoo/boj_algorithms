import heapq

n = int(input())

check = [[0] * 10 for _ in range(12)]
lst = []
zero_possible = [True] * 10

for _ in range(n):
    num = input()
    lst.append(num)

    length = len(num) - 1
    for i in range(len(num)):
        check[length][ord(num[i]) - 65] += 1
        length -= 1

    zero_possible[ord(num[0]) - 65] = False

alphabet_score = [0] * 10

temp = 1
for j in range(10):
    for i in range(12):
        alphabet_score[j] += temp * check[i][j]
        temp *= 10
    temp = 1

zero_index = alphabet_score.index(min(alphabet_score))

if not zero_possible[zero_index]:
    min_val = float("inf")
    min_idx = None
    for i in range(10):
        if zero_possible[i]:
            if alphabet_score[i] < min_val:
                min_val = alphabet_score[i]
                min_idx = i

    alphabet_score[min_idx] = 0

heap = []
for i in range(len(alphabet_score)):
    heapq.heappush(heap, [-alphabet_score[i], i])

current_score = 9
while heap:
    score, index = heapq.heappop(heap)
    alphabet_score[index] = current_score
    current_score -= 1

res = 0
for word in lst:
    real_num = ""
    for char in word:
        real_num += str(alphabet_score[ord(char) - 65])
    res += int(real_num)

print(res)