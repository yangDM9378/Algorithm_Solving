from collections import defaultdict
T=int(input())
for _ in range(T):
    check = [0] * 27
    word = input()
    k=int(input())

    word_dic = defaultdict(list)
    for i in range(len(word)):
        if word.count(word[i]) >= k:
            word_dic[word[i]].append(i)
    min_len=21e8
    max_len=-1
    if word_dic:
        for check_word in word_dic.values():
            for i in range(len(check_word)-k+1):
                check_len=check_word[i+k-1]-check_word[i]+1
                min_len=min(min_len, check_len)
                max_len=max(max_len, check_len)
        print(min_len,max_len)
    else:
        print(-1)