# 7
# 0110100
# 0110101
# 1110101
# 0000111
# 0100000
# 0111110
# 0111000


n = int(input())
matrix = []

for i in range(n):
    matrix.append(list(map(int, list(input()))))

already_included = []
count = []



def sol(i, j, matrix):
    global clusters
    global count
    global already_included

    if (i, j) not in already_included:
        already_included.append((i, j))
        clusters += 1

        if i+1 < len(matrix):
            if matrix[i + 1][j] == 1:
                sol(i + 1, j, matrix)
        if j+1 < len(matrix):
            if matrix[i][j + 1] == 1:
                sol(i, j + 1, matrix)
        if i-1 >= 0:
            if matrix[i-1][j] == 1:
                sol(i-1, j, matrix)
        if j-1 >= 0:
            if matrix[i][j-1] == 1:
                sol(i, j-1, matrix)

    else:
        return


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1 and (i, j) not in already_included:
            clusters = 0
            sol(i, j, matrix)
            count.append(clusters)

count = sorted(count)
print(len(count))
for ele in count:
    print(ele)

