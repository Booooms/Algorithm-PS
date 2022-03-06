def solution(n, left, right):
    answer = []
    for i in range(int(left),int(right+1)):
        answer.append(max(divmod(i,n))+1)
    return answer

# other solution
# def solution(n, left, right):
#     answer = []
#     for i in range(left,right+1): 
#         a,b = divmod(i,n)
#         if a<b: a,b =b,a
#         answer.append(a+1)
    
#     return answer