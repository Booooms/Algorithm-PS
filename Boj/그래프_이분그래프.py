from collections import deque

k = int(input())


def bfs(graph, start):
    queue = deque()
    queue.append(start)

    if visited[start] == 0:
        visited[start] = 1  

    while queue:
        v = queue.popleft()

        color = visited[v]
        for i in graph[v]: 
            if visited[i] == 0:
                queue.append(i)
                if color == 1: 
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:
                if color == 1:
                    print("NO")
                    return False
            elif visited[i] == 2:
                if color == 2:
                    print("NO")
                    return False
    return True

for i in range(k):
    flag = 0
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for j in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for k in range(1, V + 1):
        if not bfs(graph, k):
            flag = 1
            break
        
    if flag == 0:
        print("YES")