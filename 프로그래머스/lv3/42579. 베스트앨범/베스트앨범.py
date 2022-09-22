import heapq


def solution(genres, plays):

    genre_dict = {}

    for i in range(len(plays)):
        if genres[i] not in genre_dict.keys():
            genre_dict[genres[i]] = [0, []]
        genre_dict[genres[i]][0] += plays[i]
        heapq.heappush(genre_dict[genres[i]][1], (-plays[i], i))

    answer = []

    genre_dict = dict(sorted(genre_dict.items(), key=lambda x: x[1], reverse=True))

    for key, val in genre_dict.items():
        if val[1]:
            answer.append(heapq.heappop(val[1])[1])
        if val[1]:
            answer.append(heapq.heappop(val[1])[1])

    return answer