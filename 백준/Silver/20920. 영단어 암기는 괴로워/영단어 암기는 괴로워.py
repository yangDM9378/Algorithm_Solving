from collections import Counter
N,M = map(int, input().split())

words=[]
dict_cnt_words = {}
for _ in range(N):
    word = input()
    if M < len(word)+1:
        words.append(word)
most_sort_words = Counter(words).most_common()
for word, cnt in most_sort_words:
    dict_cnt_words[cnt] = dict_cnt_words.get(cnt, [])
    dict_cnt_words[cnt].append(word)


for len_sort_word in dict_cnt_words.values():
    len_sort_word.sort(lambda x:(-len(x),x))
    for result in len_sort_word:
        print(result)
