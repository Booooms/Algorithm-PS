import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)
        heapq.heappush(scoville, first_min + second_min*2)
        answer +=1

        if len(scoville) == 1 and scoville[0] < K:
            return -1

    return answer

# other solution
# import heapq as hq

# def solution(scoville, K):

#     hq.heapify(scoville)
#     answer = 0
#     while True:
#         first = hq.heappop(scoville)
#         if first >= K:
#             break
#         if len(scoville) == 0:
#             return -1
#         second = hq.heappop(scoville)
#         hq.heappush(scoville, first + second*2)
#         answer += 1  

#     return answer