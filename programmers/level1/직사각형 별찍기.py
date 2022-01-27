a, b = map(int, input().strip().split(' '))
for i in range(b):
    print('*' * a)

# 다른 풀이법
# a, b = map(int, input().strip().split(' '))
# print(("*" * a + "\n") * b)