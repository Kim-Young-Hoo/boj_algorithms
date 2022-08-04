import sys

g = int(input())
p = int(input())

gates = [0] * (g + 1)

for _ in range(p):

    plane = int(sys.stdin.readline().rstrip())

    if gates[plane]:
        is_possible = True
        current_gate = plane
        while True:
            if current_gate == 0:
                is_possible = False
                break

            if gates[current_gate]:
                current_gate = gates[current_gate] - 1
            else:
                gates[plane] = current_gate
                gates[current_gate] = current_gate
                break
        if not is_possible:
            break
    else:
        gates[plane] = plane


print(sum([1 for ele in gates if ele > 0]))
