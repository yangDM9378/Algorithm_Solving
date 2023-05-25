N=int(input())

li=[]
for _ in range(N):
    li.append(list(map(int, input().split(' '))))
li.sort()

for i in range(N):
    print(*li[i])
