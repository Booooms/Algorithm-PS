def sequential_search(n, target, array):
    #원소 확인
    for i in range(n):
        #찾고자 하는 원소가 동일한 경우
        if array[i] == target:
            return i + 1

print("생성할 원소 개수 입력 후, 한칸 띄고 문자열 입력하세요")
input_data = input().split()
n = int(input_data[0])
target = input_data[1]

print("앞서 적은 원소 개수 만큼 문자열 입력하세요. 구분은 띄어쓰기 한 칸입니다")
array = input().split()

print(sequential_search(n, target, array))