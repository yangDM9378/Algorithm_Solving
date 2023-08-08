from collections import deque

def bfs(y,x,maps):
    global used,cnt
    q=deque()
    q.append((y,x))
    directs=[(1,0),(-1,0),(0,1),(0,-1)]
    while q:
        y,x = q.popleft()
        for direct in directs:
            dy= y+direct[0]
            dx= x+direct[1]
            if dy<0 or dy>len(maps)-1 or dx<0 or dx>len(maps[0])-1: continue
            if maps[dy][dx]=='X' or used[dy][dx]==1:continue
            used[dy][dx]=1
            cnt+=int(maps[dy][dx])
            q.append((dy,dx))
                

def solution(maps):
    global used,cnt
    answer = []
    used=list([0]*len(maps[0]) for _ in range(len(maps)))
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x]!='X' and used[y][x]==0:
                cnt=int(maps[y][x])
                used[y][x]=1
                bfs(y,x,maps)
                answer.append(cnt)
    if len(answer)==0:
        return [-1]
    answer.sort()
    return answer