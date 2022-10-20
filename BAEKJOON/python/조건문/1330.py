a,b =map(int,input().split())

def AB(x,y):
    if x>y:
        k='>'
    elif x<y:
        k='<'
    else:
        k='=='
    
    return k

print(AB(a,b))