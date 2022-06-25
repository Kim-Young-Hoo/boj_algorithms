string = input()
pattern = input()


def lps(pattern):
    lps_lst = [0] * len(pattern)

    suffix_idx = 1
    prefix_idx = 0

    while suffix_idx < len(pattern):

        if pattern[suffix_idx] == pattern[prefix_idx]:
            prefix_idx += 1
            lps_lst[suffix_idx] = prefix_idx
            suffix_idx += 1

        else:
            if prefix_idx == 0:
                lps_lst[suffix_idx] = 0
                suffix_idx += 1
            else:
                prefix_idx = lps_lst[prefix_idx - 1]

    return lps_lst


def kmp(string, pattern):
    lps_lst = lps(pattern)

    string_idx = 0
    pattern_idx = 0

    cnt = 0
    answer_lst = []

    while string_idx < len(string):
        if string[string_idx] == pattern[pattern_idx]:
            string_idx += 1
            pattern_idx += 1
        else:
            if pattern_idx != 0:
                pattern_idx = lps_lst[pattern_idx - 1]
            else:
                string_idx += 1

        if pattern_idx == len(pattern):
            cnt += 1
            answer_lst.append(string_idx - pattern_idx + 1)
            pattern_idx = lps_lst[pattern_idx - 1]

    print(cnt)
    print(*answer_lst)


kmp(string, pattern)
