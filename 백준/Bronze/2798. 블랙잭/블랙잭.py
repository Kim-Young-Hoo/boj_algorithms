N, M = map(int, input().split(' '))
numbers = list(map(int, input().split(' ')))

def blackjack(m, lst):
	prev = 0
	for i in range(0, len(lst), 1):
		for j in range(i+1, len(lst), 1):
			for k in range(j+1, len(lst), 1):
				now = lst[i] + lst[j] + lst[k]
				if (now <= m) & (now > prev):
					prev = now
	return prev

print(blackjack(M,numbers))