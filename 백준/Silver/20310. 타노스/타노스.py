def remove_num(num, cnt, check_num):
    new_word = ''
    for i in range(len(num)):
        if num[i] == check_num:
            cnt -= 1
            if cnt == 0:
                tmp = i
                break
        else:
            new_word += num[i]
    new_word += num[tmp + 1:]
    return new_word[::-1]

num = input()
cnt_0 = 0
cnt_1 = 0
for i in range(len(num)):
    if num[i]=='0':
        cnt_0+=1
    if num[i]=='1':
        cnt_1+=1
num = remove_num(num, cnt_1//2, '1')
num = remove_num(num, cnt_0//2, '0')
print(num)