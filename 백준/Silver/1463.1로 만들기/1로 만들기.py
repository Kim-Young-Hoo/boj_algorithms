"""
input

1
2 -> 1
3 -> 1
4 -> 2 -> 1             /2
5 -> 4 -> 2 -> 1        -1
6 -> 2 -> 1             /3
7 -> 6 -> 2 -> 1        -1
8 -> 4 -> 2 -> 1        /2
9 -> 3 -> 1             /3
10 -> 9 -> 3 -> 1       -1
11 -> 10 -> 9 -> 3 -> 1 -1
12 -> 4 -> 2 -> 1       /3
13 -> 12 -> 4 -> 2 -> 1 -1
14 -> 7 -> 6 -> 2 -> 1

3가지 연산을 1번씩 해보고 그 중에서 최소인거를  return

res = [0, 1, 1, 1]
4가 들어왔으면
/3 -> 실패
/2 -> res[4/2의 몫] + 1
-1 -> res[4-1] + 1

res.append(min(res[4/2의 몫] + 1, res[4-1] + 1))
= res.append(min(1+1, 1+1))
"""

n = int(input())

def sol(n):
    res = [0, 0, 1, 1]

    if n < 4:
        return res[n]

    for i in range(4, n+1):
        temp = [res[i-1] + 1]
        if i % 3 == 0:
            temp.append(res[i//3] + 1)
        if i % 2 == 0:
            temp.append(res[i//2] + 1)
        res.append(min(temp))

    #     아마 메모리 제한 걸리는 듯해서 dp list를 줄여야 됨
    #  -1 번째꺼 냄기고, i+1 // 3


    return res[-1]

print(sol(n))
