from math import ceil, floor
def solution(a, b, g, s, w, t):
    N=len(g)
    def possible(time):
        max_gold=0
        max_silver=0
        max_weight=0
        for i in range(N):
            tmp=floor(time/t[i])
            deliver=tmp//2+tmp%2
            max_gold+=min(g[i], w[i]*deliver)
            max_silver+=min(s[i], w[i]*deliver)
            max_weight+=min(g[i]+s[i], w[i]*deliver)
        if max_gold>=a and max_silver>=b and max_weight>=a+b:
            return True
        return False
    left=0
    right=(a+b)*max(t)*2
    mid=(left+right)//2
    while left<right:
        if possible(mid):
            right=mid
        else:
            left=mid+1
        mid=(left+right)//2
    answer=right
    return answer