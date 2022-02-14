def solution(numbers):
    answer=0
    for i in range(10):
        if i not in numbers:
            answer+=i
    return answer

# other solution_1
# def solution(numbers):
#     return 45 - sum(numbers)

# other solution_2
# def solution(numbers):
#     return sum([i for i in [1,2,3,4,5,6,7,8,9,0] if i not in numbers])