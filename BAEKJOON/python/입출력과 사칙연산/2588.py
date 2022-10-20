a=int(input())
b=input()
c=b[::-1]
k=0
for i in c:
    j=a*int(i)
    k+=j
    print(j)
print(a*int(b))

