import sys
from collections import Counter
n=int(sys.stdin.readline())
arr=[]
for _ in range(n):
    arr.append(int(sys.stdin.readline()))
sor_arr=sorted(arr)
print(round(sum(sor_arr)/n))
print(sor_arr[int(n/2)])
cnt = Counter(sor_arr).most_common()
if len(cnt) > 1:
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(sor_arr[n-1]-sor_arr[0])
