n = int(input())
nums = list(map(int, input().split(' ')))
sick = list(map(int, input().split(' ')))


maximum = -1e9
minimum = 1e9


res = []

def sol(nums, sick, total):
    global maximum
    global minimum

    if sum(sick) == 0:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    for i in range(4):
        if sick[i] == 0:
            continue
        else:
            if i == 0:
                new_sick = sick.copy()
                new_sick[0] -= 1
                new_nums = nums.copy()
                pop = new_nums.pop(0)
                sol(new_nums, new_sick, total + pop)
            if i == 1:
                new_sick = sick.copy()
                new_sick[1] -= 1
                new_nums = nums.copy()
                pop = new_nums.pop(0)
                sol(new_nums, new_sick, total - pop)
            if i == 2:
                new_sick = sick.copy()
                new_sick[2] -= 1
                new_nums = nums.copy()
                pop = new_nums.pop(0)
                sol(new_nums, new_sick, total * pop)
            if i == 3:
                new_sick = sick.copy()
                new_sick[3] -= 1
                new_nums = nums.copy()
                pop = new_nums.pop(0)
                sol(new_nums, new_sick, int(total / pop))

sol(nums[1:], sick, nums[0])
print(maximum)
print(minimum)