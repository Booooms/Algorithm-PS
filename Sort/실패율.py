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

    return list(zip(*fail))[0] # 전치행렬 사용

# other solution
# def solution(N, stages):
#     answer = []
#     length = len(stages)

#     # 스테이지 번호 증가
#     for i in range(1, N+1):
#         # 스테이지에 머물러있는 사람 수 계산
#         count = stages.count(i)
#         # 실패율 계산
#         if length == 0:
#             fail = 0
#         else:
#             fail = count/length
        
#         #리스트 원소삽입
#         answer.append((i,fail))
#         length -= count
    
#     # 실패율 기준으로 내림차순 정렬
#     answer = sorted(answer, key=lambda t: t[1], reverse=True)
#     # 스테이지 번호 출력
#     answer = [i[0] for i in answer]
#     return answer


