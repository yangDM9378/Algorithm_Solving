def solution(s):
    min_cnt=len(s)
    for step in range(1,len(s)//2+1):
        new_word = ''
        target_word = s[0:step]
        cnt=1
        for i in range(step,len(s),step):
            if target_word == s[i:i+step]:
                cnt+=1
            else:
                if cnt>1:
                    new_word+=str(cnt)+target_word
                else:
                    new_word+=target_word
                target_word = s[i:i+step]
                cnt = 1
        if cnt>1:
            new_word+=str(cnt)+target_word
        else:
            new_word+=target_word

        if len(new_word) < min_cnt:
            min_cnt = len(new_word)
    return min_cnt




print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))
