def solution(record):
    answer = []
    record_dic = {}
    result =[]
    for data in record:
        arr=data.split(' ')
        if arr[0]=='Enter':
            record_dic[arr[1]]=arr[2]
            result.append(('님이 들어왔습니다.',arr[1]))
        elif arr[0]=='Leave':
            result.append(('님이 나갔습니다.',arr[1]))
        else:
            record_dic[arr[1]]=arr[2]
    for re in result:
        answer.append(f'{record_dic[re[1]]}{re[0]}')
        
    return answer