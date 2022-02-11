def solution(array, commands):
    answer = []
    for command in commands:
        com_arr = array[command[0]-1:command[1]]
        com_arr.sort()
        answer.append(com_arr[command[2]-1])
    return answer


# other solution
# def solution(array, commands):
#     answer = []
#     for command in commands:
#         i,j,k = command
#         answer.append(list(sorted(array[i-1:j]))[k-1])
#     return answer

# other solution
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))