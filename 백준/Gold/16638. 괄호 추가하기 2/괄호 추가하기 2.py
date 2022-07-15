from itertools import combinations

n = int(input())
prob = list(input())

nums = []
cals = []
plus_minus = []
multi = []

idx = 0
for ele in prob:
    if ele in ["+", "*", "-"]:
        cals.append(ele)

        if ele == "+" or ele == "-":
            plus_minus.append(idx)
        else:
            multi.append(idx)
        idx += 1

    else:
        nums.append(int(ele))


max_val = float("-inf")


def calculator(num1, num2, cal):
    if cal == "*":
        return num1 * num2
    elif cal == "+":
        return num1 + num2
    else:
        return num1 - num2



def solution(nums, cals):
    global max_val

    for i in range(len(plus_minus) + 1):
        comb = list(combinations(plus_minus, i))
        for c in comb:
            is_possible = True
            for idx in range(len(c) - 1):
                if c[idx] == c[idx + 1] - 1:
                    is_possible = False
                    break


            if is_possible:

                new_nums = [a for a in nums]
                new_cals = [ele for ele in cals]

                # 괄호 먼저 계산
                for idx in reversed(c):
                    new_nums.insert(idx, calculator(new_nums.pop(idx), new_nums.pop(idx), new_cals.pop(idx)))

                # 곱하기 계산
                multi = [i for i in range(len(new_cals)) if new_cals[i] == "*"]

                for idx in reversed(multi):
                    new_nums.insert(idx, calculator(new_nums.pop(idx), new_nums.pop(idx), new_cals.pop(idx)))

                # 나머지 계산
                answer = new_nums.pop(0)
                for idx in range(len(new_cals)):
                    answer = calculator(answer, new_nums[idx], new_cals[idx])

                max_val = max(max_val, answer)





solution(nums, cals)

print(max_val)

