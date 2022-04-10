"""
모서리 3면 나오는거 : 4개 고정 -> max([ABC, ACE, ADE, ABD, FBC, FCE, FDE, FBD])
2면 나오는 거 : N이 3일 때부터 4,12,20,... 으로 증가 -> max([AC, AB, AE, AD, BC, BD, BF, CE, CF, ED, EF, DF])
1면 나오는 거 : (n-2)*(n-2)*5 + (n-2)*4 -> max(모든 면)
"""

n = int(input())
a, b, c, d, e, f = map(int, input().split())


def solution(n, a, b, c, d, e, f):
    if n == 1:
        return sum([a, b, c, d, e, f]) - max([a, b, c, d, e, f])

    result = 0

    # 모서리 3면
    result += 4 * min([a + b + c, a + c + e, a + d + e, a + b + d, f + b + c, f + c + e, f + d + e, f + b + d])

    # 2면 나오는 거
    two_face_cnt = 4 if n > 1 else 0
    for i in range(n - 2):
        two_face_cnt += 8

    result += two_face_cnt * min([a + c, a + b, a + e, a + d, b + c, b + d, b + f, c + e, c + f, e + d, e + f, d + f])

    if n > 2:
        result += ((n - 2) * (n - 2) * 5 + (n - 2) * 4) * min([a, b, c, d, e, f])

    return result


print(solution(n, a, b, c, d, e, f))
