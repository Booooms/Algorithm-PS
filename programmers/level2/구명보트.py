def solution(people, limit):
    answer = 0
    people.sort()
    i, j = 0, len(people) - 1
    while i <= j:
        answer += 1
        if people[j] + people[i] <= limit:
            i += 1
        j-=1
    return answer

# other solution
# from collections import deque

# def solution(people, limit):
#     result = 0
#     deque_people = deque(sorted(people))

#     while deque_people:
#         left = deque_people.popleft()
#         if not deque_people:
#             return result + 1
#         right = deque_people.pop()
#         if left + right > limit:
#             deque_people.appendleft(left)
#         result += 1
#     return result