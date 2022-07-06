n = int(input())
lst = list(map(int, input().split(' ')))
lst = sorted(lst)
m = int(input())
prob = list(map(int, input().split(' ')))


def recursive_bin_search(low, high, key):
    if low == high:
        if lst[low] == key:
            return 1
        else:
            return 0

    elif low > high:
        return 0

    else:
        mid = (low + high) // 2
        if lst[mid] == key:
            return 1
        elif lst[mid] > key:
            return recursive_bin_search(low, mid - 1, key)
        else:
            return recursive_bin_search(mid + 1, high, key)


answer = []

for i in range(m):
    answer.append(recursive_bin_search(0, len(lst) - 1, prob[i]))
print(" ".join(map(str, answer)))
