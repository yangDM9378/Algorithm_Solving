def n_wls(n,k):
    n_wlstn=""
    while n:
        n_wlstn = str(n%k)+n_wlstn
        n=n//k
    return n_wlstn

import math
def prime_number(k):
    if k == 2 or k == 3: return True
    if k % 2 == 0 or k < 2: return False
    for i in range(3, int(k ** 0.5) + 1, 2):
        if k % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = -1
    n_wlstn=n_wls(n,k)
    n_wlstn=n_wlstn.split("0")
    cnt=0
    for wlstn in n_wlstn:
        if wlstn == '':continue
        cnt+=prime_number(int(wlstn))
    return cnt