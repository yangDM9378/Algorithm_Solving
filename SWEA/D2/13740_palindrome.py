import sys
sys.stdin = open("sample_input(6).txt", "r")

def z_arr():
    for i in range(n):
        for j in range(n):
            z[j][i]=arr_1[i][j]
    return z

def Wkr(a,b):
    if m%2==0:
        for k in range(n):
            arr1=a[k]
            arr2=b[k]
            for j in range(n-m+1):
                flag_1 = 0
                flag_2 = 0
                for i in range(int(m//2)):
                    if arr1[int(m//2)-1-i+j]==arr1[int(m//2)+i+j]:
                        flag_1+=1
                    if arr2[int(m//2)-1-i+j]==arr2[int(m//2)+i+j]:
                        flag_2+=1
                    if flag_1==int(m//2):
                        return arr1[int(m//2)+j-int(m//2):int(m//2)+j+int(m//2)]
                    if flag_2==int(m//2):
                        return arr2[int(m//2)+j-int(m//2):int(m//2)+j+int(m//2)]
    if m%2==1:
        for k in range(n):
            arr1=a[k]
            arr2=b[k]
            for j in range(n-m+1):
                flag_1 = 0
                flag_2 = 0
                for i in range(int(m//2)):
                    if arr1[int(m//2)-1-i+j]==arr1[int(m//2)+1+i+j]:
                        flag_1+=1
                    if arr2[int(m//2)-1-i+j]==arr2[int(m//2)+1+i+j]:
                        flag_2+=1
                    if flag_1==int(m//2):
                        return arr1[int(m//2)+j-int(m//2):int(m//2)+j+int(m//2)+1]
                    if flag_2==int(m//2):
                        return arr2[int(m//2)+j-int(m//2):int(m//2)+j+int(m//2)+1]
T=int(input())
for t in range(T):
    n,m=map(int,input().split())
    arr_1=[list(input()) for _ in range(n)]
    z=[['']*n for _ in range(n)]
    arr_2=z_arr()
    k=Wkr(arr_1,arr_2)
    a=''.join(k)
    print(f'#{t+1} {a}')

