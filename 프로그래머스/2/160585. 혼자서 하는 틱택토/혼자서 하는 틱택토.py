def check_win_cnt(board,check):
    check_cnt = 0
    # 가로
    for i in range(3):
        if board[i] == check*3:
            check_cnt += 1
    # 세로
    for i in range(3):
        word = ''
        for j in range(3):
            word += board[j][i]
        if word == check*3:
            check_cnt += 1
    # 대각선
    word = ''
    word = board[0][0]+board[1][1]+board[2][2]
    if word == check*3:
        check_cnt += 1
    # 역 대각선
    word = ''
    word = board[0][2]+board[1][1]+board[2][0]
    if word == check*3:
        check_cnt += 1
    
    return check_cnt

def solution(board):
    o_cnt=0
    x_cnt=0
    o_check_cnt = 0
    x_check_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j]=='O':
                o_cnt += 1
            elif board[i][j]=='X':
                x_cnt += 1
    print(o_cnt, x_cnt)
    
    # x갯수가 o보다 많을 때
    if o_cnt < x_cnt or o_cnt - x_cnt > 1:
        return 0

    # o가 이겼는데 ox 갯수 같을 때
    o_check_cnt = check_win_cnt(board,'O')
    x_check_cnt = check_win_cnt(board,'X')
    if o_check_cnt > 0 and x_check_cnt > 0:
        return 0
    elif o_check_cnt > 0:
        if o_cnt != x_cnt + 1:
            return 0
    elif x_check_cnt > 0:
        if o_cnt != x_cnt:
            return 0
    print(o_check_cnt, x_check_cnt)
        
    # 이기는 경우가 ox 둘다 있을때
    return 1
