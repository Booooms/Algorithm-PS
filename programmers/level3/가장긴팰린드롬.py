def solution(s):
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i

# other solution
# def solution(s):
#     return len(s) if s[::-1] == s else max(solution(s[:-1]), solution(s[1:]))