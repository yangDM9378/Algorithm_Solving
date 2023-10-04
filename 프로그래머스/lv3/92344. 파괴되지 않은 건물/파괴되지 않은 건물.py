def solution(board, skill):
    answer = 0
    tmp = [[0] *(len(board[0])+1) for _ in range(len(board)+1)]
    for t,r1,c1,r2,c2,degree in skill:
        if t==1:
            tmp[r1][c1] += -degree
            tmp[r2+1][c2+1] += -degree
            tmp[r2+1][c1] += degree
            tmp[r1][c2+1] += degree
        else:
            tmp[r1][c1] += degree
            tmp[r2+1][c2+1] += degree
            tmp[r2+1][c1] += -degree
            tmp[r1][c2+1] += -degree
    for i in range(len(tmp)):
        for j in range(1, len(tmp[0])):
            tmp[i][j] += tmp[i][j-1]
    for i in range(len(tmp[0])):
        for j in range(1, len(tmp)):
            tmp[j][i] += tmp[j-1][i]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += tmp[i][j]
            if board[i][j]>0:
                answer+=1
    return answer