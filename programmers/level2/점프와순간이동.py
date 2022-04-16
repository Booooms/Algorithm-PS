def solution(n):
    ans = 0
    while n>0:
        ans += n%2
        n//=2
            
    return ans

# other solution
# def solution(n):
#     return bin(n).count('1')