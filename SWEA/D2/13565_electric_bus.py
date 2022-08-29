import sys
sys.stdin=open("input.txt","r")


T = int(input())
for t in range(T):
    K,N,M=map(int, input().split())
    print(f'{K},{N},{M}')
    arr=list(map(int, input().split()))
    arr.append(N)
    print(arr)
    ans=0
    start=0 #몇번이동했을때 현재 시작점
    last=0 #이동후 위치
    i=0 #몇번이동하는가
    while i < len(arr):
        if arr[i]-start<=K:
            last=arr[i]
            i+=1
        else:
            if arr[i]-last>K:
                ans=0
                break
            else:
                start=last
                ans+=1
        print(f'{arr[i]},{start},{last}')
    print(f'#{t+1} {ans}')
