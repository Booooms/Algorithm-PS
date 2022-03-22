def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length # 다리를 건너고 있는 트럭
    while len(bridge):
        answer += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer

# other solution
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
#     bridge = deque(0 for _ in range(bridge_length))
#     total_weight = 0
#     step = 0
#     truck_weights.reverse()

#     while truck_weights:
#         total_weight -= bridge.popleft()
#         if total_weight + truck_weights[-1] > weight:
#             bridge.append(0)
#         else:
#             truck = truck_weights.pop()
#             bridge.append(truck)
#             total_weight += truck
#         step += 1

#     step += bridge_length

#     return step