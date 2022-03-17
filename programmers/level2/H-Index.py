def solution(citations):
    answer = 0
    citations.sort()
    for idx, citation in enumerate(citations):
        print(idx, citation)
        if citation >= len(citations) - idx :
            return len(citations) - idx
    return 0

# other solution
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer

# other solution
# def solution(citations):
#     citations = sorted(citations)
#     l = len(citations)
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0