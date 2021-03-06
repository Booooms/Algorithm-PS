def solution(participant, completion):
    participant.sort() 
    completion.sort() 
    for i in range(len(completion)):
        if(participant[i] != completion[i]):
            return participant[i]
    return participant[len(participant)-1]

# other solution - collections 사용
# import collections
# def solution(participant, completion):
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]

# other solution - hash함수 사용
# def solution(participant, completion):
#     answer = ''
#     temp = 0
#     dic = {}
#     for part in participant:
#         dic[hash(part)] = part
#         temp += int(hash(part))
#     for com in completion:
#         temp -= hash(com)
#     answer = dic[temp]
#     return answer