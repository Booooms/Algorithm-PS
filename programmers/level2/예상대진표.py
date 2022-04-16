import math
def solution(n,a,b):
    answer = 0

    while a!=b:
        answer += 1
        a = math.ceil(a/2)
        b = math.ceil(b/2)
    return answer

# other solution_1
# def solution(n,a,b):
#     return ((a-1)^(b-1)).bit_length()

# other solution_2
# def solution(n,a,b):
#     answer = 0
#     while a != b:
#         answer += 1
#         a, b = (a+1)//2, (b+1)//2

#     return answer
