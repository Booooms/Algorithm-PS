def solution(priorities, location):
    answer = 0
    queue = [(i, p) for i, p in enumerate(priorities)]
    while queue:
        flag = 0
        check = queue.pop(0)

        for x, y in queue:
            if check[1] < y:
                flag = 1

        if flag == 0:
            answer+=1
            if location == check[0]:
                break
        else:
            queue.append((check[0], check[1]))         

    return answer

# other solution
# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer