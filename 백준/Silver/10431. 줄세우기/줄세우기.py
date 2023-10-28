T=int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    cnt=0
    lines = []
    for i in range(1, 21):
        flag=False
        for j in range(len(lines)):
            if lines[j]>arr[i]:
                lines.insert(j,arr[i])
                cnt=cnt+len(lines)-j-1
                flag=True
                break
        if flag == False:
            lines.append(arr[i])
    print(arr[0], cnt)