import sys

n, m = map(int, sys.stdin.readline().split())
word_set = {}

for _ in range(n):
    word = sys.stdin.readline().strip()

    if len(word) >= m:
        if word in word_set:
            word_set[word] += 1
        else:
            word_set[word] = 1

word_dict = sorted(word_set.items(),key=lambda x:(-x[1],-len(x[0]),x[0]))

for word in word_dict:
    print(word[0])