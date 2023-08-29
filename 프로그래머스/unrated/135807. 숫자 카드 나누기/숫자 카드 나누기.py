import math
def solution(arrayA, arrayB):
    a=arrayA[0]
    b=arrayB[0]
    for i in range(len(arrayA)):
        a=math.gcd(a, arrayA[i])
        b=math.gcd(b, arrayB[i])
    
    check_A=1
    check_B=1
    for i in range(len(arrayA)):
        if arrayB[i]%a==0:
            check_B=0
        if arrayA[i]%b==0:
            check_A=0
    if check_B==0 and check_A==0:
        return 0
    else:
        return max(a,b)
    
    return 0