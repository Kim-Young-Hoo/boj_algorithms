from collections import deque


def solution(begin, target, words):
    answer = 0

    words = {word: 0 for word in words}

    if target not in words.keys():
        return 0

    queue = deque([(begin, 0)])
    words[begin] = 1

    while queue:
        word, level = queue.popleft()

        if word == target:
            return level

        for other_word, check in words.items():
            if check:
                continue

            diff_check = 0
            for i in range(len(word)):
                if word[i] != other_word[i]:
                    diff_check += 1

            if diff_check == 1:
                queue.append((other_word, level + 1))

    return answer
