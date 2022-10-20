T= int(input())

for _ in range(T):
    z_a = [0] * 4
    z_b = [0] * 4
    li_a=list(map(int, input().split()))
    li_b=list(map(int, input().split()))
    a=li_a.pop(0)
    b=li_b.pop(0)
    for i in range(a):
        z_a[li_a[i]-1]+=1
    for j in range(b):
        z_b[li_b[j]-1]+=1
    if z_a == z_b:
        print('D')
    else:
        for i in range(3,-1,-1):
            if z_a[i]>z_b[i]:
                print('A')
                break
            elif z_a[i]<z_b[i]:
                print('B')
                break
            else:
                continue


