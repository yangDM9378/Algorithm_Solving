from collections import deque
def bfs(y,x,end_y,end_x,maps):
    used=[[0]*len(maps[0]) for _ in range(len(maps))]
    q = deque()
    q.append((y,x,0))
    directs=[(-1,0),(1,0),(0,-1),(0,1)]

    while q:
        y,x,second = q.popleft()
        if y==end_y and x==end_x:
            return second
        for direct in directs:
            dy=y+direct[0]
            dx=x+direct[1]
            if dy<0 or dx<0 or dy>len(maps)-1 or dx>len(maps[0])-1: continue
            if used[dy][dx]!=0:continue
            if maps[dy][dx]=='X':continue
            used[dy][dx]=1
            q.append((dy,dx,second+1))
    return -1    

def solution(maps):
    answer = 0
    arr={}
    for y in range(len(maps)):
        for x in range(len(maps[0])):
            if maps[y][x]=='S':
                arr['S']=(y,x)
            if maps[y][x]=='L':
                arr['L']=(y,x)
            if maps[y][x]=='E':
                arr['E']=(y,x)
    min_StoL = bfs(arr['S'][0],arr['S'][1],arr['L'][0],arr['L'][1],maps)
    min_LtoE = bfs(arr['L'][0],arr['L'][1],arr['E'][0],arr['E'][1],maps)
    print(min_StoL)
    print(min_LtoE)
    if min_StoL==-1 or min_LtoE==-1:
        return -1
    else:
        return min_StoL+min_LtoE
    return answer