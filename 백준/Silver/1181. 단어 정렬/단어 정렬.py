import sys


n = int(input())
dictionary = {}

for i in range(n):
    word = sys.stdin.readline().split()[0]

    if len(word) not in dictionary.keys():
        dictionary[len(word)] = [word]
    else:
        dictionary[len(word)].append(word)

for i in range(1, 51):
    if i in dictionary.keys():
        for word in sorted(set(dictionary[i])):
            print(word)