#가게의 부품개수 입력
n = int(input())
#가게에 있는 전체 부품 번호를 집합(set) 자료형에 입력
array = set(map(int, input().split()))

#손님이 확인 요청한 부품 개수 입력
m = int(input())
#손님이 확인 요청한 전체 부품 번호를 입력
c = list(map(int, input().split()))
#손님이 확인 요청한 부품 번호 하나씩 확인
for i in c:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')