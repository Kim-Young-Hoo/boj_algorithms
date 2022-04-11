import sys

sentence = str(input())
n = int(input())
words = []
min_word_length = float("inf")

for _ in range(n):
    word = str(input())

    if len(set(word)) == 1 and list(set(word))[0] in words:
        continue
    else:
        words.append(word)
        min_word_length = min(min_word_length, len(word))

subtract_lst = []

for word in words:
    for i in range(min_word_length, len(sentence)):
        if word == sentence[i:len(word)]:
            continue
        else:
            subtract_lst.append(word)
            break

words = [x for x in words if words not in subtract_lst]


dp = {ele: float("inf") for ele in range(len(sentence)+1)}
dp[0] = 0

def solution(sentence, words):
    global min_cnt
    global dp
    global min_word_length

    idx = 0
    while idx < len(sentence):
        new_sentence = sentence[idx:]
        for word in words:
            if len(word) > len(new_sentence):
                continue
            # elif len(word) == len(new_sentence) and sorted(word) != sorted(new_sentence):
            #     return

            if sorted(new_sentence[:len(word)]) == sorted(word):
                diff = 0
                for i in range(len(word)):
                    if new_sentence[:len(word)][i] != word[i]:
                        diff += 1

                if dp[idx] != float("inf"):
                    dp[idx + len(word)] = min(dp[idx + len(word)], dp[idx] + diff)

        idx += 1

solution(sentence, words)

if dp[len(sentence)] == float("inf"):
    print(-1)
else:
    print(dp[len(sentence)])