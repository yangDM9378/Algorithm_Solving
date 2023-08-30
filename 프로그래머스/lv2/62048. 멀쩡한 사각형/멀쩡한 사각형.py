import math
def solution(w,h):
    GCD = math.gcd(w,h)
    a = w//GCD
    b = h//GCD
    return ((a-1)*(b-1)+(w-a)*b)*GCD