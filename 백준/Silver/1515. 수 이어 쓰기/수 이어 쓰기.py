num = list(input())
check_num=0
idx = 0
while True:
    check_num += 1
    for s in str(check_num):
        if num[idx] == s:
            idx+=1
            if idx >= len(num):
                print(check_num)
                exit()

