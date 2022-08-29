T=int(input())
def del_str(word):
    for i in range(1,len(word)):
        if word[i]==word[i-1]:
            word.pop(i)
            word.pop(i-1)
            return del_str(word)
    return len(word)
for t in range(T):
    word=list(input())
    print(f'#{t+1} {del_str(word)}')

