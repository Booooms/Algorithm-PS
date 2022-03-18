def solution(number, k):
    answer = [number[0]]
    for num in number[1:]:
        while len(answer) > 0 and k>0 and answer[-1] < num:
            answer.pop()
            k -= 1
        answer.append(num)
    if k != 0:
        answer = answer[:-k]
    return ''.join(answer)

# other solution
# def solution(number, k):
#     st = []
#     for i in range(len(number)):
#         while st and k > 0 and st[-1] < number[i]:
#             st.pop()
#             k -= 1
#         st.append(number[i])
#     return ''.join(st[:len(st) - k])