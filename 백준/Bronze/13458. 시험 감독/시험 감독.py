n=int(input())
arr= list(map(int, input().split()))
b,c = map(int, input().split())
answer=len(arr)

for ar in arr:
    ar=ar-b
    if ar>0:
        if ar%c==0:
            answer+=int(ar//c)
        else:
            answer+=int(ar//c)+1
print(answer)