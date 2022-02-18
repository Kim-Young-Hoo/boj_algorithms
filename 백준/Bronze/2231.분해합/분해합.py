# 자연수 모든 자리합 최대는 9*len(example)

n = int(input())


def sol(n):
    length = len(str(n))

    if length*9 > n:
        for i in range(n + 1):
            each_sum = sum(list(map(int, str(i))))
            current_sum = i + each_sum

            if current_sum == n:
                return i

    else:
        for i in range(n-9*length, n+1):
            each_sum = sum(list(map(int, str(i))))
            current_sum = i + each_sum

            if current_sum == n:
                return i

    return 0

print(sol(n))