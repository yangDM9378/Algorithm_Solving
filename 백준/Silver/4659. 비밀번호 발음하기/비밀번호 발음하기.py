mo = ['a','e','i','o','u']

# 자음 1, 모음 0
while True:
    word = input()
    con_cnt = 1
    mo_check = False
    if word == 'end':
        break
    if word[0] in mo:
        mo_check = True
        check_zamo = 0
    else:
        check_zamo = 1
    Flag = True
    for i in range(1,len(word)):
        pre_wo = word[i-1]
        if (word[i] in mo) and mo_check == False:
            mo_check = True
        if word[i] == pre_wo and (pre_wo not in ['e','o']):
            Flag=False
            break
        if (word[i] in mo) and check_zamo == 0:
            con_cnt += 1
        elif (word[i] not in mo) and check_zamo ==1:
            con_cnt += 1
        else:
            if check_zamo == 1:
                check_zamo = 0
            else:
                check_zamo = 1
            con_cnt = 1
        if con_cnt >= 3:
            Flag=False
            break
    if Flag == True and mo_check==True:
        print(f'<{word}> is acceptable.')
    else:
        print(f'<{word}> is not acceptable.')
