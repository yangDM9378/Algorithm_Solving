def solution(k, ranges):
    arr=[]
    n=0
    while True:
        if k==1:
            arr.append(k)
            break
        arr.append(k)
        n+=1
        if k%2==1:
            k=k*3+1
        elif k%2==0:
            k=k//2
    result =[]
    for x1,x2_pre in ranges:
        x2 = n+x2_pre
        if x2>n:
            x2=n
        if x1>x2:
            result.append(-1)
            continue
        elif x1==x2:
            result.append(0)
            continue
        else:
            ssum=0
            for i in range(x1,x2):
                value = (arr[i]+arr[i+1])*0.5
                ssum+= value
            result.append(ssum)
    return result