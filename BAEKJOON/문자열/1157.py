# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

a=input().upper()
li=[i for i in a]
set_li=set(li)
dic_li={}
for k in set_li:
   dic_li[k]=li.count(k)
dic_li=sorted(dic_li.items(),reverse=True, key=lambda item:item[1])
if len(li)!=1:
    if dic_li[0][1]==dic_li[1][1]:
        print('?')
    else:
        print(dic_li[0][0])
else:
    print(dic_li[0][0])


# 예제 입력 1
# Mississipi
# 예제 출력 1
# ?
# 예제 입력 2 
# zZa
# 예제 출력 2
# Z
# 예제 입력 3
# z
# 예제 출력 3
# Z
# 예제 입력 4 
# baaa
# 예제 출력 4 
# A