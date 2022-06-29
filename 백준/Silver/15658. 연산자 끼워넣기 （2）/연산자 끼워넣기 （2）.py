n = int(input())
num_lst = list(map(int, input().split(' ')))
cal_lst = list(map(int, input().split(' ')))

max_val = float("-inf")
min_val = float("inf")


def solution(n, current_idx, current_sum, cal_lst):
    global max_val
    global min_val


    if current_idx == n:
        max_val = max(current_sum, max_val)
        min_val = min(current_sum, min_val)
        return

    for i in range(4):
        if cal_lst[i] != 0:
            temp = [ele for ele in cal_lst]
            temp[i] -= 1
            temp_sum = current_sum
            if i == 0:
                temp_sum += num_lst[current_idx]
            elif i == 1:
                temp_sum -= num_lst[current_idx]
            elif i == 2:
                temp_sum *= num_lst[current_idx]
            else:
                temp_sum = int(temp_sum / num_lst[current_idx])
            solution(n, current_idx + 1, temp_sum, temp)


solution(n, 1, num_lst[0], cal_lst)
print(max_val)
print(min_val)
