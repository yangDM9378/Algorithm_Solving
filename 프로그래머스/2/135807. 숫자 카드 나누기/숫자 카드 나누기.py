import math
def solution(arrayA, arrayB):
    check_a = arrayA[0]
    check_b = arrayB[0]
    for a in arrayA[1:]:
        check_a = math.gcd(check_a, a)
    for b in arrayB:
        if b % check_a == 0:
            check_a = -1
            break
    for b in arrayB[1:]:
        check_b = math.gcd(check_b, b)
    for a in arrayA:
        if a % check_b == 0:
            check_b = -1
            break
    result = max(check_a,check_b)
    return 0 if result == -1 else result