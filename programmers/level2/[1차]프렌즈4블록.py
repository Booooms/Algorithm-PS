def solution(m, n, board): 
    answer = 0 
    
    # 지울거 찾기 
    def find(board): 
        target = set() 
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j] and board[i][j] == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                    target.update({(i, j), (i+1, j), (i, j+1), (i+1, j+1)}) 
        return target

        
    # 지우기 
    def remove(target, board): 
        board = [list(row) for row in board] 
        for loc in target: 
            i, j = loc 
            board[i][j] = '' 
        return board 
        
    # 이동하기 
    def move(board): 
        cnt = 0 
        for i in range(m-1): 
            for j in range(n): 
                if board[i][j] and not board[i+1][j]: 
                    board[i][j], board[i+1][j] = board[i+1][j], board[i][j] 
                    cnt += 1 
        return cnt, board 

    while 1: 
        target = find(board) 
        answer += len(target) 
        board = remove(target, board) 
        cnt = 1 
        while cnt: 
            cnt, board = move(board) 
        if not cnt and not len(target): 
            break 
    return answer

# other solution
# def solution(m, n, board):
#     for i in range(m):
#         board[i] = list(board[i])
    
#     cnt = 0
#     rm = set()
#     while True:
#         # 보드를 순회하며 4블록이 된 곳의 좌표를 집합에 기록
#         for i in range(m-1):
#             for j in range(n-1):
#                 t = board[i][j]
#                 if t == []:
#                     continue
#                 if board[i+1][j] == t and board[i][j+1] == t and board[i+1][j+1] == t:
#                     rm.add((i,j));rm.add((i+1,j))
#                     rm.add((i,j+1));rm.add((i+1,j+1))
        
#         # 좌표가 존재한다면 집합의 길이만큼 세주고 블록을 지움 
#         if rm:
#             cnt += len(rm)
#             for i,j in rm:
#                 board[i][j] = []
#             rm = set()
#         # 없다면 함수 종료
#         else:
#             return cnt
        
#         # 블록을 위에서 아래로 당겨줌
#         while True:
#             moved = 0
#             for i in range(m-1):
#                 for j in range(n):
#                     if board[i][j] and board[i+1][j]==[]:
#                         board[i+1][j] = board[i][j]
#                         board[i][j] = []
#                         moved = 1
#             if moved == 0:
#                 break