"""
입력 예시
a1
"""
n=input()

row=int(n[1])
col=int(ord(n[0]))- int(ord('a'))+1
direct = [[2,1],[1,2],[-2,-1],[-1,-2],[2,-1],[1,-2],[-2,1],[-1,2]]
cnt = 0
for i in direct:
    dy = row+i[0]
    dx = col+i[1]
    if 1<=dy<9 and 1<=dx<9:
        cnt+=1
print(cnt)