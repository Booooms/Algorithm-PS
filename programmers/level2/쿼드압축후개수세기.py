def solution(arr):
    h = len(arr) // 2
    if sum([sum(i) for i in arr]) == len(arr)*len(arr[0]):
        return [0, 1]
    elif sum([sum(i) for i in arr]) == 0:
        return [1, 0]
    else:
        return [sum(i) for i in zip(*[solution([i[:h] for i in arr[:h]]),
                                      solution([i[h:] for i in arr[:h]]),
                                      solution([i[:h] for i in arr[h:]]),
                                      solution([i[h:] for i in arr[h:]])])]

# other solution
# import numpy as np

# def solution(arr):
#     # 재귀함수 구현
#     def fn(a):
#         if np.all(a == 0): return np.array([1, 0])
#         if np.all(a == 1): return np.array([0, 1])
#         n = a.shape[0]//2
#         return fn(a[:n, :n]) + fn(a[n:, :n]) + fn(a[:n, n:]) + fn(a[n:, n:])

#     # 결과 리턴
#     return fn(np.array(arr)).tolist()