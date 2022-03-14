"""


example (8x8) : WBWBWBWBBWBWBWBWWBWBWBWBBWBBBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW

target  (8x8) :
        시작이 W - WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW
        시작이 B - BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB

두 문자열 for문 돌면서 바꿔야되는거만 ++1



"""








n, m = map(int, input().split(' '))

board = []

for i in range(n):
    board.append(input())


def sol(board, n, m):
    min = 65
    current_string_list = []

    start_with_w = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"
    start_with_b = "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"

    for i in range(m - 8 + 1):
        for j in range(n - 8 + 1):
            current_string = ""
            for k in range(8):
                current_string += board[j+k][i:i+8]
            current_string_list.append(current_string)


    for string in current_string_list:
        current_min_w = 0
        current_min_b = 0
        for ele1, ele2, ele3 in zip(string, start_with_w, start_with_b):
            if ele1 != ele2:
                current_min_w += 1
            if ele1 != ele3:
                current_min_b += 1

        if current_min_w <= min:
            min = current_min_w
        if current_min_b <= min:
            min = current_min_b

    return min



print(sol(board, n, m))