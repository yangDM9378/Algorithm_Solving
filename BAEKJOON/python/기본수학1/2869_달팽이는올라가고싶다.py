A,B,V=map(int, input().split())
if int((V-B)/(A-B))==(V-B)/(A-B):
    print(int((V-B)/(A-B)))
else:
    print(int((V-B)/(A-B))+1)
