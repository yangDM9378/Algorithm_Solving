N,d,k,c = map(int, input().split())
plate=[]

for _ in range(N):
    plate.append(int(input()))
for i in range(k-1):
    plate.append(plate[i])
max_cnt = 0
for i in range(N):
    check = [0] * (d + 1)
    for j in range(k):
        check[plate[i+j]]=1
    check[c]=1
    max_cnt=max(sum(check),max_cnt)
print(max_cnt)