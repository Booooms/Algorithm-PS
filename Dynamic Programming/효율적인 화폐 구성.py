#n가지 종류의 화폐와 가치의 합 m 입력
n, m = map(int, input().split())
#n개의 화폐 단위 정보 입력
array = []
for i in range(n):
    array.append(int(input()))

#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [10001] * (m+1)
#다이나믹 프로그래밍 진행(바텀업)
d[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        d[j] = min(d[j], d[j - array[i]] + 1)

#결과 출력
if d[m] == 10001: #불가능할 경우 -1출력
    print(-1)
else:
    print(d[m])