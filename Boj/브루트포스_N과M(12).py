N, M = map(int,input().split())
L = list(map(int,input().split()))
dup_check=[]

def solve(num,start,ans):
    if len(ans)==num:
        for i in ans:
            print(L[i],end=' ')
        print()
        return
    
    for i in range(start,len(L)):
        solve(num,i,ans+[i])

L=list(set(L))
L.sort()

for i in range(len(L)):
    solve(M,i,[i])