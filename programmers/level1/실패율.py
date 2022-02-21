def solution(N, stages):
    fail = []
    users = len(stages)
    for stage in range(1, N+1):
        if users != 0:
            fail_user = stages.count(stage)
            fail_rate = fail_user/users
            fail.append([stage, fail_rate])
            users -= fail_user
        else:
            fail.append([stage, 0])
    fail.sort(key = lambda x : (-x[1], x[0]))

    return list(zip(*fail))[0]

# other solution
# def solution(N, stages):
#     fail = {}
#     denominator = len(stages)
#     for stage in range(1, N+1):
#         if denominator != 0:
#             count = stages.count(stage)
#             result[stage] = count / denominator
#             denominator -= count
#         else:
#             fail[stage] = 0
#     return sorted(result, key=lambda x : result[x], reverse=True)