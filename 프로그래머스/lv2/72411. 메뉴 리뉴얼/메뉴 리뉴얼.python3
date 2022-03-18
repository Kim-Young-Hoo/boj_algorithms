from itertools import combinations


def solution(orders, course):
    answer = []

    for c in course:

        if c > max([len(ele) for ele in orders]):
            continue

        dictionary = {}

        for order in orders:
            perm = combinations(order, c)
            for p in perm:
                joined_menu = ''.join(sorted(list(p)))
                if joined_menu not in dictionary:
                    dictionary[joined_menu] = 1
                else:
                    dictionary[joined_menu] += 1

        max_key = []
        max_selected = max(dictionary.values())
        for key, item in dictionary.items():
            if item == max_selected and max_selected > 1:
                max_key.append(key)

        if max_key:
            for ele in max_key:
                answer.append(ele)

    return sorted(answer)


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]

print(solution(orders, course))
