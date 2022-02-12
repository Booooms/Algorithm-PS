from itertools import combinations 
def check(a, b, c): 
    total = a + b + c
    for i in range(2, total): 
        if total % i == 0 : return False 
    return True 

def solution(nums):
    answer = 0
    com_list = list(combinations(nums, 3))
    for i in com_list: 
        if check(i[0], i[1], i[2]): answer += 1
    return answer

# other solution
# from itertools import combinations
# def prime_number(x):
#     answer = 0
#     for i in range(1,int(x**0.5)+1):
#         if x%i==0:
#             answer+=1
#     return 1 if answer==1 else 0

# def solution(nums):
#     return sum([prime_number(sum(c)) for c in combinations(nums,3)])