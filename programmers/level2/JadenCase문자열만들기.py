def solution(s):
    answer = ''
    s_split = s.split(" ")
    for i in s_split:
        i = i.capitalize()
        if answer == "":
            answer = i
        else:
            answer = answer + " " + i
    
    return answer

# other solution
# def solution(s):
#     return s.title()