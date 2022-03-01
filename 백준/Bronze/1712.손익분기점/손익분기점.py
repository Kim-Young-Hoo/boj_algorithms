a,b,c = map(int,input().split(' '))

if b>=c:
	print(-1)

#break_point = a + n * (b - c)
else:
	n = -a / (b - c) + 1
#-1000/-100

	print(int(n))
