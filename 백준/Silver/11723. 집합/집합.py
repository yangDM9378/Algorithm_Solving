import sys
t=int(input())
result = set()
for _ in range(t):
    word = sys.stdin.readline().strip().split()
    if word[0]=='all':
        result = {'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'}
    elif word[0]=='empty':
        result=set()
    else:
        a,b=word[0],word[1]
        if a=='add':
            result.add(b)
        elif a=='remove':
            result.discard(b)
        elif a=='check':
            if b in result:
                print(1)
            else:
                print(0)
        elif a=='toggle':
            if b in result:
                result.discard(b)
            else:
                result.add(b)

