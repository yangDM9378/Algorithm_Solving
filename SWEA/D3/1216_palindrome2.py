import sys
sys.stdin = open("input_2.txt", "r")

def z_arr():
    for i in range(n):
        for j in range(n):
            z[j][i]=arr_1[i][j]
    return z

def Wkr(a):
    for m in range(99, -1, -1):
        if m%2==0:
            for k in range(n):
                arr1=a[k]
                for j in range(n-m+1):
                    flag_1 = 0
                    for i in range(int(m//2)):
                        if arr1[int(m//2)-1-i+j]!=arr1[int(m//2)+i+j]:break
                        flag_1+=1
                    if flag_1==int(m//2):
                        return m
        if m%2==1:
            for k in range(n):
                arr1=a[k]
                for j in range(n-m+1):
                    flag_1 = 0
                    for i in range(int(m//2)):
                        if arr1[int(m//2)-1-i+j]!=arr1[int(m//2)+1+i+j]:break
                        flag_1+=1
                        if flag_1==int(m//2):
                            return m

for _ in range(10):
    t=int(input())
    n=100
    arr_1=[list(input()) for _ in range(n)]
    z=[['']*n for _ in range(n)]
    arr_2=z_arr()
    li = []
    k1=Wkr(arr_1)
    k2=Wkr(arr_2)
    li.append(k1)
    li.append(k2)
    print(f'#{t} {max(li)}')


