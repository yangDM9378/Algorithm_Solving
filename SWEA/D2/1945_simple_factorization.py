
T=int(input())

for t in range(T):
    cnt_2 = 0
    cnt_3 = 0
    cnt_5 = 0
    cnt_7 = 0
    cnt_11 = 0
    n=int(input())
    while 1:
        if n%2==0:
            n=n/2
            cnt_2+=1
        elif n%3==0:
            n=n/3
            cnt_3+=1
        elif n%5==0:
            n=n/5
            cnt_5+=1
        elif n%7==0:
            n=n/7
            cnt_7+=1
        elif n%11==0:
            n=n/11
            cnt_11+=1
        else:
            break
    print(f'#{t+1} {cnt_2} {cnt_3} {cnt_5} {cnt_7} {cnt_11}')