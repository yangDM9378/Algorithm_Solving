# 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.

T=int(input())
for i in range(T):
    a,b=map(str,input().split())
    re=''
    for j in b:
        k=j*int(a)
        re=re+k
    print(re)

# 예제 입력 1
# 2
# 3 ABC
# 5 /HTP
# 예제 출력 1 
# AAABBBCCC
# /////HHHHHTTTTTPPPPP