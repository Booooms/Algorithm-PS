def solution(brown, yellow):
    answer = []
    total = brown + yellow                 
    for b in range(1,total+1):
        if (total / b) % 1 == 0:            
            a = total / b
            if a >= b:                      
                if 2*a + 2*b == brown + 4:   
                    return [a,b]
            
    return answer

# other solution
# def solution(brown, yellow):
#     for i in range(1, int(yellow**(1/2))+1):
#         if yellow % i == 0:
#             if 2*(i + yellow//i) == brown-4: 꼭짓점개수 빼기(겹치는부분)
#                 return [yellow//i+2, i+2]