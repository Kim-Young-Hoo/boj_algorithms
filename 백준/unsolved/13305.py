n = int(input())
meter = list(map(int,input().split(" ")))
city = list(map(int, input().split(" ")))


"""
4
2 3 1
5 2 4 1

5에서 2번 = 10
2에서 4번 = 8

-> 18


4
3 3 4
1 1 1 1

-> 10


비싼거라면 앞에 가야되는거만큼만 사고 
싼거에서 살수있을만큼 사고


"""

def sol(n, meter, city):

    cost = 0

    last_calculated_index = len(city)
    for i in reversed(range(len(city)-1)):

        # 현재 도시보다 낮은 가격의 도시가 앞에 남아있다면
        if city[i] != min(city[:i+1]):
            continue

        elif city[i] == min(city[:i+1]):
            cost += city[i] * sum(meter[i:last_calculated_index])
            last_calculated_index = i

    return cost

print(sol(n, meter, city))