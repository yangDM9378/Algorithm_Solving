def solution(board):
    n=len(board)
    m=len(board[0])
    for i in range(1,n):
        for j in range(1,m):
            if board[i][j] == 1:
                board[i][j]= min(board[i-1][j],board[i][j-1],board[i-1][j-1])+1
    max_board=0
    for i in range(n):
        for j in range(m):
            max_board = max(max_board, board[i][j])
    return max_board**2