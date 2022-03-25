def solution(progresses, speeds):
    answer = []
    cnt = 0 # 작업끝난 횟수
    days = 0 # 작업기간

    while len(progresses) > 0:
        if progresses[0]+days*speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            days += 1
    answer.append(cnt)
    return answer
        
# other solution
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]