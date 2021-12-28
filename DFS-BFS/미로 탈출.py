#DFS/BFS 실전문제4 미로 탈출
from collections import deque

n, m = map(int, input().split())
#2차원 리스트 맵 입력
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    #queue 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        #현재 위치에서 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
                continue
            #벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            #노드를 처음 방문했을 경우 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    #최단거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))