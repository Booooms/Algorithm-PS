from itertools import combinations

def solution(relation):
    row = len(relation)
    col = len(relation[0])

    #가능한 속성의 모든 인덱스 조합 
    combi = []
    for i in range(1, col+1):
        combi.extend(combinations(range(col), i))
        
    #유일성
    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:    # 유일성
            put = True
            
            for x in unique:
                if set(x).issubset(set(i)):  # 최소성
                    put = False
                    break
                    
            if put: unique.append(i)
   
    return len(unique)

# other solution

# def solution(relation):
#     answer_list = list()
#     for i in range(1, 1 << len(relation[0])):
#         tmp_set = set()
#         for j in range(len(relation)):
#             tmp = ''
#             for k in range(len(relation[0])):
#                 if i & (1 << k):
#                     tmp += str(relation[j][k])
#             tmp_set.add(tmp)

#         if len(tmp_set) == len(relation):
#             not_duplicate = True
#             for num in answer_list:
#                 if (num & i) == num:
#                     not_duplicate = False
#                     break
#             if not_duplicate:
#                 answer_list.append(i)
#     return len(answer_list)