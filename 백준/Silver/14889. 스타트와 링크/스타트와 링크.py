from itertools import combinations

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split(' '))))

comb = list(combinations(range(0, n), n // 2))


min_val = float("inf")

for k in range(0, len(comb) // 2):
    team_a = comb[k]
    team_b = [ele for ele in range(0, n) if ele not in team_a]

    team_a_sum = 0
    for i in range(0, len(team_a) - 1):
        for j in range(i + 1, len(team_a)):
            team_a_sum += matrix[team_a[i]][team_a[j]]
            team_a_sum += matrix[team_a[j]][team_a[i]]
    team_b_sum = 0
    for i in range(0, len(team_a) - 1):
        for j in range(i + 1, len(team_a)):
            team_b_sum += matrix[team_b[i]][team_b[j]]
            team_b_sum += matrix[team_b[j]][team_b[i]]

    min_val = min(min_val, abs(team_a_sum - team_b_sum))

print(min_val)
