from collections import deque


def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)

    index_dict = {enroll[i]: i for i in range(len(enroll))}

    for i in range(len(amount)):
        stack = deque([seller[i]])
        earning = amount[i] * 100

        while stack:
            pop = stack.pop()
            ten_percent = earning * 0.1
            if ten_percent >= 1:
                answer[index_dict[pop]] += earning - int(ten_percent)
                earning = int(ten_percent)
            else:
                answer[index_dict[pop]] += earning
                break

            if referral[index_dict[pop]] != '-':
                stack.append(referral[index_dict[pop]])

    return answer


solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
         ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"],
         [12, 4, 2, 5, 10])
