# 예전에는 운영체제에서 크로아티아 알파벳을 입력할 수가 없었다. 따라서, 다음과 같이 크로아티아 알파벳을 변경해서 입력했다.
# 크로아티아 알파벳	변경
# č     c=
# ć     c-
# dž    dz=
# đ     d-
# lj	lj
# nj	nj
# š	    s=
# ž	    z=

words=input()
li=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in li:
    words=words.replace(i,'&')
print(len(words))


# 예제 입력 1
# ljes=njak
# 예제 출력 1
# 6
# 예제 입력 2 
# ddz=z=
# 예제 출력 2
# 3
# 예제 입력 3
# nljj
# 예제 출력 3
# 3
# 예제 입력 4
# c=c=
# 예제 출력 4
# 2
