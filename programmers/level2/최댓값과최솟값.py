def solution(s):
    answer = list(map(int, s.split(' ')))
    return '{} {}'.format(min(answer), max(answer))

# other solution
# def solution(s):
# answer = list(map(int, s.split()))
# return str(min(answer)) + " " + str(max(answer))