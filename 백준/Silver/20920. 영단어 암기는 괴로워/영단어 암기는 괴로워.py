N,M = map(int, input().split())
word_set = {}

for _ in range(N):
    word = input()
    if len(word) >= M:
        word_set[word] = word_set.get(word,1)+1
word_dict = sorted(word_set.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))
for word in word_dict:
    print(word[0])