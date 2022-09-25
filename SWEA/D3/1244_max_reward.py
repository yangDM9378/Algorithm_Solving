def dfs(level):
    global arr
    global result
    global li
    a=''
    if level==n:
        for k in range(len(arr)):
            a+=arr[k]
        if int(a)>=result:
            result=int(a)
        return

    if ''.join(arr) in li[level]:
        return
    li[level].append(''.join(arr))

    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            if ''.join(arr) not in li[level]:
                dfs(level+1)
            arr[i], arr[j] = arr[j], arr[i]

T=int(input())
for t in range(T):
    word, n=map(int, input().split())
    arr=list(str(word))
    result=-1111
    li=[[] for _ in range(n)]
    dfs(0)
    print(f'#{t+1} {result}')
