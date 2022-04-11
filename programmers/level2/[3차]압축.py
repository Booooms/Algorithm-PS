def solution(msg):
    answer = []
    d = dict()
    for c in range(ord('A'), ord('Z') + 1):
        d[chr(c)] = c - ord('A') + 1
    idx = 27
    start, end = 0, 1

    while end < len(msg) + 1:
        s = msg[start:end]
        if s in d:
            end += 1
        else:
            answer.append(d[s[:-1]])
            d[s] = idx
            idx += 1
            start = end - 1
    answer.append(d[s])
    return answer

# other solution
# def solution(msg):
#     alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
#     answer = []

#     while True:
#         if msg in d:
#             answer.append(d[msg])
#             break
#         for i in range(1, len(msg)+1):
#             if msg[0:i] not in d:
#                 answer.append(d[msg[0:i-1]])
#                 d[msg[0:i]] = len(d)+1
#                 msg = msg[i-1:]
#                 break

#     return answer

