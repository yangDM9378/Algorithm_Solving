a=int(input())

def score(x):
    if x>=90:
        k='A'
    elif x>=80:
        k='B'
    elif x>=70:
        k='C'
    elif x>=60:
        k='D'
    else:
        k='F'
    return k

print(score(a))
