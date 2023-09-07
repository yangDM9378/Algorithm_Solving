from collections import deque
def bfs(y,x,board):
    n=len(board)
    m=len(board[0])
    used = [[[] for _ in range(m)] for _ in range(n)]
    q=deque()
    q.append((y,x,0))
    directs = [(-1,0),(1,0),(0,1),(0,-1)]
    while q:
        y,x,cnt = q.popleft()
        if board[y][x]=='G':
            return cnt
        for i in range(4):
            if i in used[y][x]:continue
            diry=directs[i][0]
            dirx=directs[i][1]
            while True:
                dy=y+diry
                dx=x+dirx
                if dy<0 or dx<0 or dy>n-1 or dx>m-1:
                    used[y][x].append(i)
                    q.append((dy-directs[i][0],dx-directs[i][1],cnt+1))
                    break
                if board[dy][dx]=='D':
                    used[y][x].append(i)
                    q.append((dy-directs[i][0],dx-directs[i][1],cnt+1))
                    break
                diry+=directs[i][0]
                dirx+=directs[i][1]
    return -1

def solution(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]=='R':
                answer = bfs(y,x,board)
        
    return answer