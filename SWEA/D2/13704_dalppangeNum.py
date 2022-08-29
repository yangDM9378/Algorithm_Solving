T=int(input())
for t in range(T):
    n=int(input())
    arr=[[0]*n for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    x=0
    y=0
    dir=0
    num = 1
    while num<=n*n:
        arr[y][x]=num
        x=x+dx[dir]
        y=y+dy[dir]

        if x<0 or x>n-1 or y<0 or y>n-1 or arr[y][x]!=0:
            x=x-dx[dir]
            y=y-dy[dir]
            dir=(dir+1)%4
            x=x+dx[dir]
            y=y+dy[dir]
        num+=1
    print(f'#{t+1}')
    for i in range(n):
        for j in range(n):
            print(arr[i][j],end=' ')
        print()