num = input()
cnt_0 = num.count('0')/2
cnt_1 = num.count('1')/2
new_num=''
for i in range(len(num)):
    if num[i]=='1' and cnt_1 == 0:
        new_num+='1'
    elif num[i]=='1' and cnt_1 !=0:
        cnt_1-=1
    if num[i]=='0' and cnt_0 != 0:
        cnt_0-=1
        new_num+='0'
print(new_num)