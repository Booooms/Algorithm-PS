def solution(s):
    answer = True
    s_list = []
    for c in s:
        if c == '(':
            s_list.append(c)
        else:
            if s_list == []:
                return False
            else:
                s_list.pop()
    if s_list != []:
        answer = False
    return answer

# other solution
# def solution(s):
#     x = 0
#     for w in s:
#         if x < 0:
#             break
#         x = x+1 if w == "(" else x-1 if w == ")" else x
#     return x==0