def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

# other solution
# from itertools import combinations
# def solution(numbers):
#    return sorted(set(sum(i) for i in list(combinations(numbers, 2))))