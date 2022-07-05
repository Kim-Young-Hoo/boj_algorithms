n = int(input())

matrix = []
max_day = 0
for _ in range(n):
    a, b = map(int, input().split(' '))
    max_day = max(b, max_day)

    matrix.append([b, a])

matrix = sorted(matrix, key=lambda x: x[0], reverse=True)

answer = 0

for i in range(max_day, 0, -1):
    current_max_val = 0
    current_max_index = -1
    for j in range(len(matrix)):
        if matrix[j][0] < i:
            break
        if matrix[j][1] > current_max_val:
            current_max_val = matrix[j][1]
            current_max_index = j

    if not current_max_index == -1:
        matrix.pop(current_max_index)
    answer += current_max_val

print(answer)
