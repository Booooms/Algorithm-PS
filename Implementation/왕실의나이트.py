pos = input()

row = int(pos[1]) # 숫자 '1' -> 1
col = int(ord(pos[0])) - 96 # 문자 ord함수는 문자 -> 아스키코드값
#(row=y, col=x)
result = 0

distance = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (-1,2), (1,-2), (-1,-2)]

# dis = (2,1)
for dis in distance:
    print(dis)
    row_go = row + dis[1]
    col_go = col + dis[0]

    if row_go <= 8 and row_go > 0 and col_go <= 8 and col_go > 0:
        result += 1

print(result)
