from collections import deque

def solution(board):
    n=len(board)
    used=[[[21e8] * n for _ in range(n)] for _ in range(4)]
    q=deque()
    q.append((0,0,0,0))
    q.append((0,0,1,0))
    while q:
        y,x,state,money = q.popleft()
        directs = [(0,1,0),(1,0,1),(0,-1,2),(-1,0,3)]
        for direct in directs:
            dy=y+direct[0]
            dx=x+direct[1]
            if dy<0 or dx<0 or dy>n-1 or dx>n-1:continue
            if board[dy][dx]!=0:continue
            new_money=money+1
            if state != direct[2]:
                new_money=new_money+5
            if used[direct[2]][dy][dx]>new_money:
                used[direct[2]][dy][dx]=new_money
                if dy==n-1 and dx==n-1:continue
                q.append((dy,dx,direct[2],new_money))
    result =21e8
    for i in range(4):
        result = min([result, used[i][n-1][n-1]])
    return result*100