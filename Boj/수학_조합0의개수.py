N, M = map(int, input().split())

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

five_count = count_number(N, 5) - count_number(M, 5) - count_number(N - M, 5)
two_count = count_number(N, 2) - count_number(M, 2) - count_number(N - M, 2)

answer = min(five_count, two_count)
print(answer)

# other solution
# def countNum(N, num):
#     count = 0
#     divNum = num
#     while( N >= divNum):
#         count = count + (N // divNum)
#         divNum = divNum * num
#     return count

# M, N = map(int, input().split())
# print(min(countNum(M, 5) - countNum(N, 5) - countNum(M-N, 5), countNum(M, 2) - countNum(N, 2) - countNum(M-N, 2)))
