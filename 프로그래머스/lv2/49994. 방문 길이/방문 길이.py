def solution(dirs):
    dirs_dic = {'U':[-1,0], 'D':[1,0], 'R':[0,1], 'L':[0,-1]}
    y=5
    x=5
    cnt=0
    s = set()
    for go in dirs:
        dy=y+dirs_dic[go][0]
        dx=x+dirs_dic[go][1]
        if dy<0 or dx<0 or dy>10 or dx>10:continue
        s.add((y,x,dy,dx))
        s.add((dy,dx,y,x))
        y,x = dy,dx
    return len(s)//2