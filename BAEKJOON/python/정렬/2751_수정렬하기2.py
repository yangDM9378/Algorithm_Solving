N=int(input())
li=[]
for _ in range(N):
    li.append(int(input()))
li.sort(reverse=False)
for i in range(N):
    print(li[i])