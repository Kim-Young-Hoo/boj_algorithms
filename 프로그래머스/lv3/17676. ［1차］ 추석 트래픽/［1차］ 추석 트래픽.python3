import datetime


# print(datetime.datetime.strptime("2016-09-15 01:00:04.002", '%Y-%m-%d %H:%M:%S.%f')-datetime.timedelta(seconds=2-0.001))


def solution(lines):
    answer = 0

    lines = [
        [(datetime.datetime.strptime(ele.split(' ')[0] + " " + ele.split(' ')[1],
                                     '%Y-%m-%d %H:%M:%S.%f') - datetime.timedelta(
            seconds=float(ele.split(' ')[2][:-1]) - 0.001)).timestamp(),
         datetime.datetime.strptime(ele.split(' ')[0] + " " + ele.split(' ')[1], '%Y-%m-%d %H:%M:%S.%f').timestamp()]
        for ele
        in lines
    ]

    start_time = lines[0][0]

    cnt_list = []

    for i in range(len(lines)):
        section = [start_time, start_time + 1 - 0.001]
        cnt = 0
        for start, end in lines:
            if section[0] <= end <= section[1]:
                cnt += 1
            elif section[0] <= start <= section[1]:
                cnt += 1
        cnt_list.append(cnt)
        start_time = lines[i][0]


    start_time = lines[0][1]

    for i in range(len(lines)):
        section = [start_time, start_time + 1 - 0.001]
        cnt = 0
        for start, end in lines:
            if section[0] <= end <= section[1]:
                cnt += 1
            elif section[0] <= start <= section[1]:
                cnt += 1
            elif section[0] >= start and section[1] <= end:
                cnt += 1
        cnt_list.append(cnt)
        start_time = lines[i][1]

    answer = max(cnt_list)
    return answer


lines =["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]

print(solution(lines))
