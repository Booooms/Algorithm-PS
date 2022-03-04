def solution(n):
    cnt_n = bin(n).count('1')
    for i in range(n+1, 1000001):
        if bin(i).count('1') == cnt_n:
            return i