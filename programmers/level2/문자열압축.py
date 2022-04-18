def solution(s):
    answer = len(s)
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):
        k = s[0:i]
        
        result = ""
        cnt = 1
        for j in range(i, len(s), i):
            if k == s[j:j+i]:
                cnt += 1
            else:
                if cnt >= 2:
                    result += str(cnt) + k
                else:
                    result+=k
                
                k = s[j:j+i]
                cnt = 1
        if cnt >= 2:
            result += str(cnt) + k
        else:
            result+=k
        
        answer = min(answer, len(result))  
        
    return answer