from itertools import combinations


def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    lst1 = {}
    lst2 = {}

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            if str1[i] + str1[i + 1] in lst1.keys():
                lst1[str1[i] + str1[i + 1]] += 1
            else:
                lst1[str1[i] + str1[i + 1]] = 1

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            if str2[i] + str2[i + 1] in lst2.keys():
                lst2[str2[i] + str2[i + 1]] += 1
            else:
                lst2[str2[i] + str2[i + 1]] = 1


    joint = []
    whole = []

    for key, item in lst1.items():
        if key in lst2.keys():
            if lst1[key] >= lst2[key]:
                joint.extend([key]*lst2[key])
                whole.extend([key]*lst1[key])
            else:
                joint.extend([key]*lst1[key])
                whole.extend([key]*lst2[key])
        else:
            whole.extend([key] * lst1[key])

    for key, item in lst2.items():
        if key in lst1.keys():
            if key not in joint:
                if lst1[key] >= lst2[key]:
                    joint.extend([key]*lst2[key])
                    whole.extend([key]*lst1[key])
                else:
                    joint.extend([key]*lst1[key])
                    whole.extend([key]*lst2[key])
        else:
            if key not in whole:
                whole.extend([key] * lst2[key])

    if len(whole) == 0:
        return 65536
    return int((len(joint) / len(whole)) * 65536)

print(solution("abc", 'abbb'))