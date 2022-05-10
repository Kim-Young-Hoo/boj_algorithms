n = int(input())

lst = []
for _ in range(n):
    lst.append(list(map(int, input().split(' '))))

lst = list(reversed(lst))
dp = [0] * n

def solution(lst):
    for i in range(len(lst)):
        if lst[i][0] - i > 1:
            continue
        else:
            max_dp = max(dp[:i-lst[i][0]+1]) if dp[:i-lst[i][0]+1] else 0
            dp[i] = lst[i][1] + max_dp
    return max(dp)

print(solution(lst))
