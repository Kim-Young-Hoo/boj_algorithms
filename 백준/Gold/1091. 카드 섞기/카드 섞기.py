n = int(input())  # 3의 배수 <= 48
card_lst = list(range(n))
p = list(map(int, input().split(' ')))  # 각 카드가 어느 플레이어에게 가야되는지
s = list(map(int, input().split(' ')))  # 각 카드가 섞여서 어디 위치로 가야되는지


def solution(card_lst, p, s):
    status_lst = [ele % 3 for ele in card_lst]
    seen = []

    idx = 0
    while True:
        if status_lst == p:
            break

        idx += 1
        new_card_lst = [0] * len(card_lst)

        for i in range(len(s)):
            new_card_lst[i] = card_lst[s[i]]

        if new_card_lst == seen:
            return -1

        card_lst = new_card_lst
        status_lst = [ele % 3 for ele in card_lst]

        if not seen:
            seen = card_lst

    return idx


print(solution(card_lst, p, s))
