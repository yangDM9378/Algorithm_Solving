def solution(clothes):
    dic = {}
    for name, catagory in clothes:
        if catagory not in dic:
            dic[catagory] = 1
        else:
            dic[catagory] += 1
    cnt = 1
    for key, value in dic.items():
        cnt *= value+1
    return cnt-1