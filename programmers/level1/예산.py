def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

# other solution(time complexity: O(n))
# def solution(d, budget):
#     d.sort()
#     for i in range(len(d)):
#         budget -= d[i]
#         if budget < 0 : return i
#     return len(d)