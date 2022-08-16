import sys

n = int(input())

s = []
for _ in range(n):
    s.append(sys.stdin.readline().rstrip())
    # s.append("A")

left = 0
right = n - 1
t = ""
while left <= right:
    if s[left] > s[right]:
        t += s[right]
        right -= 1
    elif s[left] < s[right]:
        t += s[left]
        left += 1
    else:
        current_left = left
        current_right = right
        broke = False
        while current_left <= current_right:
            if s[current_right] == s[current_left]:
                current_left += 1
                current_right -= 1
            elif s[current_right] > s[current_left]:
                t += s[left]
                left += 1
                broke = True
                break
            else:
                t += s[right]
                right -= 1
                broke = True
                break
        if not broke:
            t += s[right]
            right -= 1


for i in range(0, len(t), 80):
    print(t[i:i + 80])
