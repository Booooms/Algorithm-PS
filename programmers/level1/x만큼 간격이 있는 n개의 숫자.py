def solution(x, n):
    array = []
    for i in range(1, n+1):
        array.append(x*i)
    return array

# other solution
# def solution(x, n):
#     return [i*x + x for i in range(n)]
