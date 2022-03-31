import math


def turret(x1,y1,r1,x2,y2,r2):

    #각 원점 사이의 직선거리
    dist = math.sqrt((x1 - x2)**2 + (y2 - y1)**2)
    lst = [dist, r1, r2]
    lst = sorted(lst)
    
    
    if x1==x2 and y1==y2 and r1==r2:
        return -1
    
    elif dist == (r1 + r2) or abs(r1-r2) == dist:
        return 1

    elif lst[2] > lst[0] + lst[1]:
        return 0
    
    else:
        return 2


    
n = int(input())


for i in range(n):
	x1,y1,r1,x2,y2,r2 = map(int,input().split(' '))
	print(turret(x1,y1,r1,x2,y2,r2))
    

