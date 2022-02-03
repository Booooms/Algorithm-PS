def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        return True
    else:
        return False

# other solution
# def solution(s):
#     return s.isdigit() and len(s) in (4, 6)