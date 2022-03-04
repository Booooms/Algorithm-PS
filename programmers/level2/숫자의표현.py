def solution(n):
    answer = 1
    for i in range(1, n//2 + 1):
        cnt = 0
        for j in range(i, n+1): 
            cnt += j 
            if cnt == n: 
                answer += 1
                break
            elif cnt > n: break 
    return answer

# other solution
# def solution(num):
#     return len([i  for i in range(1,num+1,2) if num % i is 0])