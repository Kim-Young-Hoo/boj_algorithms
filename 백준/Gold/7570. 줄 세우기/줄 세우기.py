n = int(input())
lst = list(map(int, input().split(' ')))
idx_lst = [0] * (n + 1)

for i in range(n):
    idx_lst[lst[i]] = i

max_length = 0

check = [False] * (n + 1)
for i in range(n):
    if not check[i]:
        length = 1
        current_num = lst[i]
        check[current_num] = True
        for j in range(0, n):
            next_num = current_num + 1
            if next_num >= n:
                break
            if idx_lst[current_num] < idx_lst[next_num]:
                length += 1
                current_num = next_num
            else:
                break
        max_length = max(length, max_length)

print(n - max_length)
