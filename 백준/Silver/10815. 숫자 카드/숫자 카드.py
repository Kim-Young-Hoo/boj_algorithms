n = int(input())
cards = list(map(int, input().split(' ')))
cards = sorted(cards)
cards.insert(0, float("-inf"))
m = int(input())
prob = list(map(int, input().split(' ')))



def check(x, index):
    return x <= cards[index]


def solution(x):
    low = 0
    high = len(cards) - 1

    while low + 1 < high:
        mid = (low + high) // 2

        if check(x, low) == check(x, mid):
            low = mid
        else:
            high = mid

    if x == cards[low]:
        return "1"

    if x == cards[high]:
        return "1"
    else:
        return "0"


answer = []
for x in prob:
    answer.append(solution(x))
print(" ".join(answer))