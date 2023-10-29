n,m=map(int, input().split())

check_arr = []
for _ in range(n):
    check_arr.append(list(map(int,input().split())))

check_arr.sort(key=lambda x:(-x[1],-x[2],-x[3]))

for i in range(len(check_arr)):
    if check_arr[i][0]==m:
        result = i
        break
for j in range(result-1,-1,-1):
    if check_arr[result][1:] == check_arr[j][1:]:
        result-=1
    else:
        break
print(result+1)