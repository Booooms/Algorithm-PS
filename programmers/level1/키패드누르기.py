def solution(numbers, hand):
    answer = ''
    left_num = 10
    right_num = 12
    
    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            left_num = num
        elif num in [3,6,9]:
            answer += 'R'
            right_num = num
        else:
            num = 11 if num == 0 else num
            
            absL = abs(num-left_num)
            absR = abs(num-right_num)
        
            if sum(divmod(absL, 3)) > sum(divmod(absR, 3)):
                answer += 'R'
                right_num = num
            
            elif sum(divmod(absL, 3)) < sum(divmod(absR, 3)):
                answer += 'L'
                left_num = num
            
            else:
                if hand == 'left':
                    answer += 'L'
                    left_num = num
                else:
                    answer += 'R'
                    right_num = num
        
    return answer