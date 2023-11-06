n=int(input())
switches = list(map(int, input().split()))

t=int(input())
for _ in range(t):
    gender,num = map(int, input().split())
    num=num-1
    if gender == 1:
        for i in range(num,n,num+1):
            if switches[i] == 0:
                switches[i]=1
            else:
                switches[i]=0
    else:
        cnt=0
        for i in range(1,n//2):
            if num-i < 0 or num+i > (n-1):
                break
            else:
                if switches[num-i] == switches[num+i]:
                    cnt+=1
                else:
                    break
        for i in range(num-cnt,num+cnt+1):
            if switches[i] == 0:
                switches[i] = 1
            else:
                switches[i] = 0
for i in range(n):
    print(switches[i])