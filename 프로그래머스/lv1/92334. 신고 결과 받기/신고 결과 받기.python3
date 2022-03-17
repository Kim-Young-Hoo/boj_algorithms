def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))

    user_report_list = {ele: [] for ele in id_list}
    report_count_list = {ele: 0 for ele in id_list}

    for ele in report:
        user, report = ele.split(' ')
        user_report_list[user].append(report)
        report_count_list[report] += 1

    for user in report_count_list:
        if report_count_list[user] >= k:
            report_count_list[user] = True
        else:
            report_count_list[user] = False

    i = 0
    for user in user_report_list:
        for ele in user_report_list[user]:
            if report_count_list[ele]:
                answer[i] += 1
        i += 1


    return answer


