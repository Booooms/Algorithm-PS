import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    #가장작은 2개 꺼내기
    one_min = heapq.heappop(heap)
    two_min = heapq.heappop(heap)
    # 합치고 삽입
    sum_value = one_min + two_min
    result += sum_value
    heapq.heappush(heap, sum_value)
print(result)
