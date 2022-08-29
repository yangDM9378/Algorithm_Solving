
T=int(input())

def color_num(a):
    for i in range(a[0],a[2]+1):
        for j in range(a[1],a[3]+1):
            z_arr[i][j]+=a[4]
    return z_arr

for t in range(T):
    n=int(input())
    z_arr = [[0] * 10 for _ in range(10)]
    arr=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        a=arr[i]
        z_arr=color_num(a)

    cnt=0
    for k in range(10):
        for z in range(10):
            if z_arr[k][z]==3:
                cnt+=1
    print(f'#{t+1} {cnt}')