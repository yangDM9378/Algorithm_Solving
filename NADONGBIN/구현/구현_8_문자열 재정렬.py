"""
입력에시
K1KA5CB7

입력예시
AJKDLSI412K4JSJ9D
"""

arr= list(input())
string_word = []
num=-1
for word in arr:
    if word.isdigit()==False:
        string_word.append(word)
    else:
        num+=int(word)
string_word.sort()
if len(arr) !=len(string_word):
    string_word.append(str(num+1))

print(''.join(string_word))
