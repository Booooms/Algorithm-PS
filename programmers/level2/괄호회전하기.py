def solution(s):
    answer = 0
    temp=list(s)

    for _ in range(len(s)):
        stack = []
        for i in range(len(temp)):
            if len(stack) > 0:
                if stack[-1] == '[' and temp[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and temp[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and temp[i] == '}':
                    stack.pop()
                else:
                    stack.append(temp[i])
            else:
                stack.append(temp[i])
        if len(stack) == 0:
            answer += 1
        temp.append(temp.pop(0))
    return answer

# other solution
# from collections import deque

# def check(string):
#     stack = []
#     for s in string:
#         if len(stack) == 0:
#             if s == ')' or s == '}' or s == ']':
#                 return False
#         if s == '(' or s == '{' or s == '[':
#             stack.append(s)
#         else:
#             if s == ')' and stack[-1] == '(':
#                 stack.pop()
#             elif s == '}' and stack[-1] == '{':
#                 stack.pop()
#             elif s == ']' and stack[-1] == '[':
#                 stack.pop()
#     if stack:
#         return False
#     else:
#         return True

# def solution(s):
#     answer = 0
#     queue = deque(list(s))
#     i = 0
#     while i != len(queue):
#         if check(queue):
#             answer += 1
#         queue.rotate(-1)
#         i += 1

#     return answer