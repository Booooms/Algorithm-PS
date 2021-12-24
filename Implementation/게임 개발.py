n, m = map(int, input().split())
x, y, direction = map(int, input().split())

#전체 맵 정보 입력
map_list = []
for i in range(n):
    map_list.append(list(map(int, input().split())))

# 방향 정의
# 북:0 동:1 남:2 서:3
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#방문처리 체크
check = [[0 for i in range(m)] for j in range(n)]
check[x][y] = 1 #초기 좌표 방문처리
#방향 카운트
turn_count = 0
count = 1

#시작
while True:
    direction -= 1
    if direction < 0:
        direction = 3

    nx = x + dx[direction]
    ny = y + dy[direction]

    if map_list[nx][ny] == 0 and check[nx][ny] == 0:
        check[nx][ny] = 1
        x = nx
        y = ny
        turn_count = 0
        count += 1
        continue
    #회전한 이후 가보지않은 칸이 없거나 바다인 경우
    else:
        turn_count += 1
    # 모든 방향 갈 수 없는 경우
    if turn_count == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 이동
        if map_list[nx][ny] == 0:
            x = nx
            y = ny
        #뒤가 바다인 경우
        else:
            break
        turn_count = 0

print(count)