n = int(input())
arr = list(map(int ,input().split()))
visited = [False]*n
answer = 0

def sol(li):
    global answer #전역변수 선언
    if len(li) == n:
        total = 0
        for i in range(n-1):
            total += abs(li[i]- li[i+1])
        answer = max(answer, total)
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            li.append(arr[i])
            sol(li)
            visited[i] = False
            li.pop()

sol([])
print(answer)


# 라이브러리 사용
from itertools import permutations
 
n = int(input())
a = list(map(int, input().split()))
 
per = permutations(a)
ans = 0
 
for i in per:
    s = 0
    for j in range(len(i)-1):
        s += abs(i[j]-i[j+1])
    if s > ans:
        ans = s
 
print(ans)