def ischeck(m,n,board):
    check_board = [(0,1),(1,0),(1,1)]
    used=[[0]*n for _ in range(m)]
    checked_cnt = 0
    for i in range(m-1):
        for j in range(n-1):
            if board[i][j]!='x':
                check_cnt = 0
                for check in check_board:
                    if board[i][j] == board[i+check[0]][j+check[1]]:
                        check_cnt+=1
                if check_cnt == 3:
                    used[i][j]=1
                    for check in check_board:
                        used[i+check[0]][j+check[1]]=1
    for i in range(m):
        for j in range(n):
            if used[i][j]==1:
                board[i][j]='x'
                checked_cnt+=1
    if checked_cnt == 0:
        return 0
    
    for j in range(n):
        for i in range(m-1, -1, -1):
            if board[i][j] == 'x':
                k = i
                while k-1 >= 0 and board[k-1][j] == 'x':
                    k -= 1
                if k-1>=0:
                    board[i][j] = board[k-1][j]
                    board[k-1][j] = 'x'

    return checked_cnt


def solution(m, n, board):
    answer = 0
    board = list(map(list, board))
    while True:
        check_cnt = ischeck(m,n,board)
        if check_cnt == 0:
            break
        answer+=check_cnt
                
    return answer