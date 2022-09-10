li=['+','-','*','/']
T= int(input())

def forth(arr):
    if len(arr)<2:
        return -1
    if len(arr)==2:
        k1=arr.pop()
        k2=arr.pop()
        if k2=='.':
            if k1 not in li:
                return k1
            return -1
        else:
            return -1
    stack=[]
    stack.append(arr.pop())
    stack.append(arr.pop())
    while arr:
        k=arr.pop()
        if k=='.':
            if len(stack)==1:
                return stack.pop()
            else:
                return -1
        elif k in li:
            if len(stack) >= 2:
                b=stack.pop()
                a=stack.pop()
                if k=='+':
                    c=int(a)+int(b)
                    stack.append(str(c))
                elif k=='-':
                    c=int(a)-int(b)
                    stack.append(str(c))
                elif k=='*':
                    c=int(a)*int(b)
                    stack.append(str(c))
                elif k=='/':
                    c=int(a)//int(b)
                    stack.append(str(c))
            else:
                return -1
        else:
            stack.append(k)

for t in range(1,T+1):
    arr=list(input().split())
    arr=arr[::-1]
    k=forth(arr)
    if k==-1:
        print(f'#{t} error')
    else:
        print(f'#{t} {int(k)}')