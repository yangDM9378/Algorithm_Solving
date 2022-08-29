T=int(input())
arr=list(map(int, input().split()))
li=[]
for i in range(1,T+1):
    li.insert(len(li)-arr[i-1],i)
print(*li)
