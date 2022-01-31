def gcdlcm(n, m):
    a, b = max(n, m), min(n, m)
    t=1
    while t>0:
        t = a%b
        a, b = b, t
    answer = [a, int(n*m/a)]
    return answer