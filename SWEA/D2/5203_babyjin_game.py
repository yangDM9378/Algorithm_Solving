
def run_g(li,a):
    for i in range(2,10):
        if li[i-2]!=0 and li[i-1]!=0 and li[i]!=0:
            return a
    for k in range(10):
        if li[k] == 3:
            return a
    return 0


T=int(input())
for t in range(T):
    arr=list(map(int, input().split()))
    li_0=[0]*10
    li_1=[0]*10
    ret=0
    for i in range(0,len(arr),2):
        li_0[arr[i]]+=1
        li_1[arr[i+1]]+=1
        ret+=run_g(li_0,1)
        if ret!=0:
            print(f'#{t+1} {ret}')
            break
        ret+=run_g(li_1,2)
        if ret!=0:
            print(f'#{t+1} {ret}')
            break
    if ret==0:
        print(f'#{t+1} {ret}')