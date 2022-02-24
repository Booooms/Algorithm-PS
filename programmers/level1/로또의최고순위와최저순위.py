def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    win_cnt = 0
    cnt_0 = lottos.count(0)
            
    for i in win_nums:
        if i in lottos:
            win_cnt += 1
            
    high_score = rank[cnt_0 + win_cnt]
    low_score = rank[win_cnt]
    
    return [high_score, low_score]
    # return rank[cnt_0 + win_cnt], rank[win_cnt]