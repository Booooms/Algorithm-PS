def solution(s):
    answer = []
    bin_cnt = 0
    zero_cnt = 0
    while s != "1":
        zero_cnt += s.count("0")
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        bin_cnt += 1
    answer = [bin_cnt, zero_cnt]
    return answer