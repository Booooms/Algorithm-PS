#hash.get, values() 사용
def solution(clothes):
    hash_map = {} 
    for clothe, type in clothes: 
        hash_map[type] = hash_map.get(type, 0) + 1 
        # if type not in hash_map:
        #     hash_map[type] = 2
        # else:
        #     hash_map[type] += 1
        
    answer = 1 
    for type in hash_map: 
        answer *= (hash_map[type] + 1) 
    # answer = 1
    # for num in hash_map.values():
    #     answer *= num
    
    return answer - 1

#values(), 인덱스 사용
# def solution(clothes):
#     answer = {}
#     for i in clothes:
#         if i[1] in answer: answer[i[1]] += 1
#         else: answer[i[1]] = 1

#     cnt = 1
#     for i in answer.values():
#         cnt *= (i+1)
#     return cnt - 1

# #counter 사용
# def solution(clothes):
#     from collections import Counter
#     from functools import reduce
#     cnt = Counter([kind for name, kind in clothes])
#     answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
#     return answer