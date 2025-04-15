def solution(s):
    arr = []
    s=s[1:-1]
    li = ''
    for i in s:
        if i == '{':
            li=''
        elif i == '}':
            arr.append(list(li.split(',')))
            li=''
        else:
            li+=i
    arr.sort(key=lambda x:len(x))
    answer = []
    for li in arr:
        for num in li:
            if int(num) not in answer:
                answer.append(int(num))
    return list(answer)