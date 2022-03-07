def solution(word):
    n = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}

    answer = len(word)
    re = (((5 + 1)*5 + 1)*5 + 1)*5 + 1
    for i in word:
        answer += re * n[i]
        re = (re - 1) // 5

    return answer
    
# other solution
# def solution(word):
#     answer = 0
#     for i, n in enumerate(word):
#         answer += (5 ** (5 - i) - 1) / (5 - 1) * "AEIOU".index(n) + 1
#     return answer