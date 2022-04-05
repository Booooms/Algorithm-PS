def solution(name):
    answer = 0
    min_move = len(name) - 1
    
    for idx, char in enumerate(name):
        # 알파벳 변경 최솟값
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        next_idx = idx + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1 
        
        
        min_move = min([min_move, idx*2 + len(name) - next_idx, idx + 2*(len(name) -next_idx)])
    answer += min_move
    return answer