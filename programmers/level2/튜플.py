def solution(s):
    answer = []
    sp_s = (s[2:-2].split('},{'))
    sp_s.sort(key=len)
    for i in sp_s:
        list_s = list(map(int, i.split(',')))
        for j in list_s:
            if j not in answer:
                answer.append(j)
    return answer

# other solution
# from collections import Counter
# def solution(s):
#     new_s = [sss.replace('{','').replace('}','') for sss in s.split(',')]
#     return [int(c[0]) for c in sorted(Counter(new_s).items(), key = lambda x: x[1],reverse=True )]