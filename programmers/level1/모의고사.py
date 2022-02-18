def solution(answers):
    answer = []
    student_1 = [1,2,3,4,5] * 2000
    student_2 = [2,1,2,3,2,4,2,5] * 1250
    student_3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    first_cnt = second_cnt = third_cnt = 0
    
    for i in range(len(answers)):
        if student_1[i] == answers[i]:
            first_cnt += 1
        if student_2[i] == answers[i]:
            second_cnt += 1
        if student_3[i] == answers[i]:
            third_cnt += 1
    # for i, a, b, c in zip(answers, student_1, student_2, student_3):
    #     if i == a:
    #         first_cnt += 1
    #     if i == b:
    #         second_cnt += 1
    #     if i == c:
    #         third_cnt += 1    
    
    arr_cnt = [first_cnt, second_cnt, third_cnt]
    max_cnt = max(arr_cnt)
    for k, value in enumerate(arr_cnt):
        if value == max_cnt:
            answer.append(k+1)

    return sorted(answer)

# other solution
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []

#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1

#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)

#     return result