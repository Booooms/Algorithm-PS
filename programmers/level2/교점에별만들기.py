def solution(line):
    pos = []
    answer = []
    n = len(line)

    x_min, y_min = int(1e15),int(1e15)
    x_max, y_max = -int(1e15), -int(1e15)
    
    for i in range(n):
        a,b,e = line[i]
        for j in range(i+1,n):
            c,d,f = line[j]
            if a*d == b*c :
                continue
            x = (b*f-e*d) / (a*d-b*c)
            y = (e*c-a*f) / (a*d-b*c)

            if x == int(x) and y == int(y):
                x = int(x)
                y = int(y)
                pos.append([x,y])
                if x_min > x :
                    x_min = x
                if y_min > y:
                    y_min = y
                if x_max < x:
                    x_max = x
                if y_max < y :
                    y_max = y

    x_len = x_max-x_min+1
    y_len = y_max-y_min+1
    arr = [['.']*x_len for _ in range(y_len)]

    for star_x, star_y in pos:
        nx = star_x + abs(x_min) if x_min < 0 else star_x - x_min
        ny = star_y + abs(y_min) if y_min < 0 else star_y - y_min
        arr[ny][nx]='*'

    for i in range(len(arr)-1,-1,-1):
        answer.append(''.join(arr[i]))

    return answer


# other solution
# from itertools import combinations as combi
# def solution(line):
#     n_list = [i for i in range(len(line))]
#     start_points = []
#     x_list, y_list = [], []

#     #별 찍는 위치
#     for i, j in combi(n_list,2):
#         a, b, e = line[i]
#         c, d, f = line[j]
#         if(a*d - b*c):
#             x = (b*f-e*d) / (a*d-b*c)
#             y = (e*c-a*f) / (a*d-b*c)
#             if x.is_integer() and y.is_integer():
#                 start_points.append((int(x), int(y)))
#                 x_list.append(int(x))
#                 y_list.append(int(y))
    
#     # x, y의 최대 최솟값과 배열의 크기 구하기
#     max_x, min_x = max(x_list), min(x_list)
#     max_y, min_y = max(y_list), min(y_list)
#     x_size = max_x - min_x + 1
#     y_size = max_y - min_y + 1

#     arr = [['.'] * x_size for _ in range(y_size)]
#     for x, y in start_points:
#         arr[max_y-y][x-min_x] = "*"

#     return [''.join(s) for s in arr]
