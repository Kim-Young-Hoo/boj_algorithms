"""
[
[0,0,0,0,0],
[0,0,1,0,3],
[0,2,5,0,1],
[4,2,4,4,2],
[3,5,1,3,1]
]


"""


def solution(board, moves):
    stack = []
    count = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                toy = board[i][move-1]
                board[i][move-1] = 0
                stack.append(toy)
                break

        if len(stack) > 1 and stack[-1] == stack[-2]:
            stack = stack[:-2]
            count += 2

    return count


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board=board, moves=moves))
