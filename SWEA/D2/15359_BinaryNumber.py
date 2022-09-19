T=int(input())
dict={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
for t in range(T):
    n, word_16=input().split()
    word_10=0
    for i in range(int(n)):
        if word_16[i].isdigit():
            k=word_16[i]
            word_10+=int(k)*16**(int(n)-(i+1))
        else:
            k=dict[word_16[i]]
            word_10+=k*16**(int(n)-(i+1))
    word_2=bin(word_10)[2:]
    result='0'*(4*int(n)-len(word_2))+word_2
    print(f'#{t+1} {result}')
W