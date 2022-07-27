import math
T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    lcm = (a*b) // math.gcd(a,b)
    print(lcm)


# other solution
# 유클리드 호제법으로 구하기
# T = int(input())

# for _ in range(T):
#     a, b = map(int, input().split())
#     aa, bb = a, b

#     while a%b != 0:
#         a, b = b, a%b
#     print(aa*bb/b)