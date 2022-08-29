T=int(input())
k=['{','}','(',')']

def zzzz(a):
    global stack_li
    if len(stack_li)==0:
        stack_li.append(a.pop())
    else:
        if stack_li[-1]=='}' and a[-1]=='{':
            stack_li.pop()
            a.pop()
        elif stack_li[-1]==')'and a[-1]=='(':
            stack_li.pop()
            a.pop()
        else:
            stack_li.append(a.pop())
    return a




for t in range(T):
    arr=list(input())
    a=[]
    for i in range(len(arr)):
        if arr[i] in k:
            a.append(arr[i])

    # if len(a)%2==1:
    #     print(0)

    stack_li = []
    while len(a)>0:
        a=zzzz(a)

    if len(stack_li)==0:
        print(f'#{t+1} 1')
    else:
        print(f'#{t+1} 0')

