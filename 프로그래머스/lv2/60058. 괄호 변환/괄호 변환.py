
def collect_word(word):
    stack = []
    for i in range(len(word)):
        if word[i] == '(':
            stack.append('(')
        else:
            if len(stack)==0:
                return False
            stack.pop()
    return True
        
def divide_uv(p):
    cnt_dhls=0
    cnt_dh=0
    for i in range(len(p)):
        if p[i]=='(':
            cnt_dhls+=1
        else:
            cnt_dh+=1
        if cnt_dhls == cnt_dh:
            u=p[:i+1]
            v=p[i+1:]
            return u,v

def solution(p):
    if len(p) == 0:
        return ''
    u,v=divide_uv(p)
    print(u,v)
    if collect_word(u):
        return u+solution(v)
    
    else:
        new_word='('
        new_word+=solution(v)
        new_word+=')'
        for i in range(1,len(u)-1):
            if u[i]==')':
                new_word+='('
            else:
                new_word+=')'
    return new_word