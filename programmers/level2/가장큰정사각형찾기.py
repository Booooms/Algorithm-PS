def solution(board):
    n = len(board) # 세로
    m = len(board[0]) # 가로

    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(1,n):
        dp[i][0] = board[i][0]
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    # 최대 넓이 구하기
    answer = 0
    for i in range(n):
        temp = max(dp[i])
        answer = max(answer, temp)
    return answer**2
    
# other solution
# def solution(board):
#     answer = 1 if 1 in board[0] or 1 in board[-1] else 0
#     for m in range(1,len(board)):
#         for n in range(1,len(board[0])):
#             if board[m][n] == 1:
#                 board[m][n] = min(board[m-1][n], board[m-1][n-1], board[m][n-1]) + 1
#                 if board[m][n] > answer:
#                     answer = board[m][n]
#     return answer ** 2