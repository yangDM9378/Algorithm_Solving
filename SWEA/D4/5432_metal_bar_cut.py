T=int(input())
for t in range(T):
    word=input()
    word=word.replace('()','1')
    arr=list(word)
    stack=[]
    answer=0
    for i in range(len(arr)):
        if arr[i]=='(':
            stack.append(arr[i])
        elif arr[i]=='1':
            answer+=len(stack)
        elif arr[i]==')':
            stack.pop()
            answer+=1
    print(f'#{t+1} {answer}')