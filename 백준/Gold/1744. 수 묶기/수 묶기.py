"""
1. 음수가 여러개 있다면 큰 음수끼리 곱해야 됨
2. 양수도 곱해서 넣어야 됨
3. 곱해서 남는 음수가 있고, 0이 있다면 둘이 곱해서 없애야 됨
4. 곱해서 남는 음수가 있고, 0이 없다면 그냥 빼셈
"""

import heapq

n = int(input())
positive_lst = []
negative_lst = []

zero_cnt = 0
for i in range(n):
    num = int(input())
    if num == 0:
        zero_cnt += 1
    elif num > 0:
        heapq.heappush(positive_lst, -num)
    else:
        heapq.heappush(negative_lst, num)

cum_sum = 0

while positive_lst:
    if len(positive_lst) >= 2:
        a = -heapq.heappop(positive_lst)
        b = -heapq.heappop(positive_lst)
        multiply = a * b
        plus = a + b

        if multiply > plus:
            cum_sum += multiply
        else:
            cum_sum += plus
    elif len(positive_lst) == 1:
        cum_sum += -heapq.heappop(positive_lst)

while negative_lst:
    if len(negative_lst) >= 2:
        cum_sum += heapq.heappop(negative_lst) * heapq.heappop(negative_lst)
    elif len(negative_lst) == 1:
        if zero_cnt > 0:
            break
        else:
            cum_sum += heapq.heappop(negative_lst)

print(cum_sum)
