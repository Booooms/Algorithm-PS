def solution(n, lost, reserve):
    dis_reserve = []
    dis_lost = []
    for i in reserve:
        if i not in lost:
            dis_reserve.append(i)
    for j in lost:
        if j not in reserve:
            dis_lost.append(j)
    # dis_reserve  = [i for i in reserve if i not in lost]
    # dis_lost = [j for j in lost if j not in reserve]
    dis_reserve.sort()
    dis_lost.sort()
    for i in dis_reserve:
        front = i - 1
        back = i + 1
        if front in dis_lost:
            dis_lost.remove(front)
        elif back in dis_lost:
            dis_lost.remove(back)
    
    return n - len(dis_lost)

# other solution
# def solution(n, lost, reserve):
#     reserve_ = set(reserve) - set(lost)
#     lost_ = set(lost) - set(reserve)
    
#     for person in reserve_:
#         if person -1 in lost_:
#             lost_.remove(person-1)
#         elif person+1 in lost_:
#             lost_.remove(person+1)
    
#     return n - len(lost_)