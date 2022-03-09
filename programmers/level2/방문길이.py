def solution(dirs):
    visited = set()
    x, y = 0, 0
    for i in dirs:
        if i == 'L' and x > -5:
            visited.add(((x-1, y), (x, y)))
            i -= 1
        elif i == 'R' and x < 5:
            visited.add(((x, y), (x+1, y)))
            x += 1
        elif i == 'U' and y < 5:
            visited.add(((x, y), (x, y+1)))
            y += 1
        elif i == 'D' and y > -5:
            visited.add(((x, y-1), (x, y)))
            y -= 1
    return len(visited)

# other solution
# def solution(dirs):
#     s = set()
#     d = {'U': (0,1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
#     x, y = 0, 0
#     for i in dirs:
#         nx, ny = x + d[i][0], y + d[i][1]
#         if -5 <= nx <= 5 and -5 <= ny <= 5:
#             s.add((x,y,nx,ny))
#             s.add((nx,ny,x,y))
#             x, y = nx, ny
#     return len(s)//2