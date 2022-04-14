n = int(input())


def solution(n):
    cnt = 0
    sieve = [True] * (n + 1)

    sosu_lst = []

    left_pointer = 0

    current_sum = 0

    for i in range(2, n + 1):

        if sieve[i]:

            sosu_lst.append(i)
            current_sum += i

            if current_sum == n:
                cnt += 1

            for j in range(i + i, n + 1, i):
                sieve[j] = False

            if current_sum > n:  # left 움직여야됨

                while current_sum >= n:
                    current_sum -= sosu_lst[left_pointer]
                    left_pointer += 1
                    if current_sum == n:
                        cnt += 1
    return cnt


print(solution(n))
