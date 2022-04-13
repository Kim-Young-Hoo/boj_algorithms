n = int(input())
price_list = list(map(int, input().split(' ')))
num_list = list(range(n))

price_list, num_list = zip(*sorted(zip(price_list, num_list)))

m = int(input())

# print(price_list, num_list)


def solution(price_list, num_list, money):
    floor = []

    for i in range(len(price_list)):
        if money - price_list[i] >= 0 and num_list[i] != 0:
            floor = [num_list[i]]
            money = money - price_list[i]
            break

    while money >= price_list[0]:
        floor.append(num_list[0])
        money -= price_list[0]

    for idx, ele in enumerate(floor):
        max_num = ele
        m_change = 0

        for i in range(len(num_list)):
            if money - (price_list[i] - price_list[num_list.index(ele)]) >= 0:
                if num_list[i] > max_num:
                    max_num = num_list[i]
                    m_change = price_list[i] - price_list[num_list.index(ele)]
        floor[idx] = max_num
        money -= m_change

    if not floor or floor[0] == 0:
        return 0

    return ''.join(map(str, floor))

print(solution(price_list, num_list, m))
