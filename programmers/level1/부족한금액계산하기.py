def solution(price, money, count):
    result = 0
    answer = 0
    for i in range(1, count+1):
        result += i*price
    answer = result - money
    return answer if answer > 0 else 0

# other solution
# def solution(price, money, count):
#     return max(0, price*(count+1)*count//2-money)