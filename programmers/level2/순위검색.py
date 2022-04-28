def solution(info, query):
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    for k in data:
        data[k].sort()

        # print(k, data[k])

    answer = list()
    for q in query:
        q = q.split()

        pool = data[(q[0], q[2], q[4], q[6])]
        find = int(q[7])
        l = 0
        r = len(pool)
        mid = 0
        while l < r:
            mid = (r+l)//2
            if pool[mid] >= find:
                r = mid
            else:
                l = mid+1
            # print(l, r, mid, answer)
        # answer.append((pool, find, mid))
        answer.append(len(pool)-l)

    return answer


# other solution
# from itertools import combinations
# from collections import defaultdict
# from bisect import bisect_left

# def solution(info, query):
#     answer = []
#     dic = defaultdict(list)

#     for i in info:
#         i = i.split()
#         condition = i[:-1]
#         score = int(i[-1])
#         for i in range(5):
#             case = list(combinations([0,1,2,3], i))
#             for c in case:
#                 tmp = condition.copy()
#                 for idx in c:
#                     tmp[idx] = "-"
#                 key = ''.join(tmp)
#                 dic[key].append(score) 

#     for value in dic.values():
#         value.sort()   

#     for q in query:
#         q = q.replace("and ", "")
#         q = q.split()
#         target_key = ''.join(q[:-1])
#         target_score = int(q[-1])
#         cnt = 0
#         if target_key in dic:
#             target_list = dic[target_key]
#             idx = bisect_left(target_list, target_score)
#             cnt = len(target_list) - idx
#         answer.append(cnt)      
#     return answer