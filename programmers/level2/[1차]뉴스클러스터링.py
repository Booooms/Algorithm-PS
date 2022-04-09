from collections import Counter

def solution(str1, str2):

    result1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()]
    result2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()]

    if not result1 and not result2:
        return 65536

    c1 = Counter(result1)
    c2 = Counter(result2)
    answer = int(float(sum((c1&c2).values()))/float(sum((c1|c2).values())) * 65536)
    return answer

# other solution_1
# import re
# import math

# def solution(str1, str2):
#     str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
#     str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

#     gyo = set(str1) & set(str2)
#     hap = set(str1) | set(str2)

#     if len(hap) == 0 :
#         return 65536

#     gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
#     hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

#     return math.floor((gyo_sum/hap_sum)*65536)


# other solution_2
# from collections import Counter

# def solution(str1, str2):

#     result1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if str1[i:i+2].isalpha()]
#     result2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if str2[i:i+2].isalpha()]

#     tlist = set(result1) | set(result2)
#     hap = [] #합집합
#     gyo = [] #교집합

#     if tlist:
#         for n in tlist:
#             hap.extend([n]*max(result1.count(n), result2.count(n)))
#             gyo.extend([n]*min(result1.count(n), result2.count(n)))

#         answer = int(len(gyo)/len(hap)*65536)
#         return answer

#     else:
#         return 65536