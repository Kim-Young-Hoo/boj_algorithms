def solution(routes):
    answer = 1
    
    routes = sorted(routes, key=lambda x: x[1])
    
    last_end = routes.pop(0)[1]
    for start, end in routes:
        if start <= last_end:
            continue
        elif start > last_end:
            last_end = end
            answer += 1
    
    return answer