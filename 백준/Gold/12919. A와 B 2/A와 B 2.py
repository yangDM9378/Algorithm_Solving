def dfs(level, word):
    global s,t,check
    if check != 0:
        return
    if level==len(s):
        if word == s:
            check=1
        return
    if word[-1]=='A':
        dfs(level-1, word[:-1])
    if word[0]=='B':
        dfs(level-1, word[1:][::-1])

s=input()
t=input()
check=0
dfs(len(t), t)
print(1) if check==1 else print(0)