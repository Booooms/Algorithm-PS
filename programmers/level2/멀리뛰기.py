def solution(n):
    dp = [1] + [0 for i in range(n)]
    
    dp[0], dp[1] = 1, 2
    for i in range(2, n):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567

    return dp[n-1]

# other solution
# def jumpCase(num):
#     a, b = 1, 2
#     for i in range(2,num):
#         a, b = b, a+b
#     return b

# def jumpCase(num):
#     answer = 0
#     if num==1:
#         return 1
#     elif num==2:
#         return 2
#     else:
#         return jumpCase(num-1)+jumpCase(num-2)