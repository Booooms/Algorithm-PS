def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dic_report = {id: [] for id in id_list}

    for report in set(report):
        report = report.split(' ')
        dic_report[report[1]].append(report[0])

    for key, value in dic_report.items():
        if len(value) >= k:
            for x in value:
                answer[id_list.index(x)] += 1
    return answer

# other solution
# def solution(id_list, report, k):
#     answer = [0] * len(id_list)    
#     reports = {x : 0 for x in id_list}

#     for r in set(report):
#         reports[r.split()[1]] += 1

#     for r in set(report):
#         if reports[r.split()[1]] >= k:
#             answer[id_list.index(r.split()[0])] += 1

#     return answer