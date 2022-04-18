from math import gcd
def solution(w,h):
    gcd_wh = gcd(w,h)
    answer = w*h-(w+h-gcd_wh)
    return answer