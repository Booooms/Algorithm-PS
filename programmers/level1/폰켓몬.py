def solution(nums):
    result = 0
    p = len(nums)/2
    ponketmon = set(nums)
    if len(ponketmon) > p:
        result = p
    else:
        result = len(ponketmon)
    return result

# other solution
# def solution(nums):
#     return min(len(nums)/2, len(set(nums)))