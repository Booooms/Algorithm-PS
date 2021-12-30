array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #리스트의 원소가 하나 이하라면 종료
    if len(array) <= 1:
        return array

    pivot = array[0] #피벗은 첫번째 원소
    tail = array[1:] #피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] #왼쪽 부분 분할
    right_side = [x for x in tail if x > pivot] #오른쪽 부분 분할

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))