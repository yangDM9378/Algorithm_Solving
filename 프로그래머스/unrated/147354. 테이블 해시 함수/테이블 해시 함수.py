def solution(data, col, row_begin, row_end):
    answer = []
    data.sort(key=lambda x:(x[col-1],-x[0]))
    for i in range(row_begin,row_end+1):
        sum_mods=0
        for value in data[i-1]:
            sum_mods += value%i
        answer.append(sum_mods)
    
    result = answer[0]
    for k in range(1,len(answer)):
        result = int(bin(result^answer[k])[2:],2)
        
    return result