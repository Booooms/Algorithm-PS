#가게의 부품개수 입력
n = int(input())
array = [0] * 1000001

#가게에 있는 전체 부품 번호를 입력
for i in input().split():
    array[int(i)] = 1

#손님이 확인 요청한 부품 개수 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 입력
c = list(map(int, input().split()))
#손님이 확인 요청한 부품 번호 하나씩 확인
for i in c:
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')