def solution(fees, records):
    answer = []
    records_dic={}
    result = {}
    
    for record in records:
        time, num, state = map(str, record.split())
        hour, minute = map(int, time.split(':'))
        if state == "IN":
            records_dic[num] = [hour, minute]
            if num not in result.keys():
                result[num] = 0
        else:
            in_out_time = (hour-records_dic[num][0])*60+minute-records_dic[num][1]
            result[num] += in_out_time
            records_dic[num]=[]

    for num in records_dic:
        if records_dic[num] != []:
            in_out_time = (23-records_dic[num][0])*60+59-records_dic[num][1]
            print(in_out_time)
            result[num] += in_out_time

    sort_result = sorted(result.items())
    print(sort_result)
    for item in sort_result:
        chance = item[1]-fees[0]
        print(chance)
        if chance <=0:
            answer.append(fees[1])
        else:
            if chance//fees[2] != chance/fees[2]:
                ceil = chance//fees[2]+1
            else:
                ceil = chance//fees[2]
            money = fees[1]+ceil*fees[3]
            answer.append(money)
    return answer