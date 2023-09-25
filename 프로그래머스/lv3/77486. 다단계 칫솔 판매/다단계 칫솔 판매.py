def solution(enroll, referral, seller, amount):
    answer = {}
    result = {'-':0}
    for i in range(len(enroll)):
        answer[enroll[i]] = referral[i]
        result[enroll[i]]=0
    for i in range(len(seller)):
        current_money = amount[i]*100
        if current_money >= 10:
            my_money=int(current_money*0.9)
            rest=int(current_money*0.1)
        else:
            my_money = current_money
            rest = 0
        result[seller[i]]+=my_money
        check_man = answer[seller[i]]
        while True:
            current_money = rest
            if current_money >= 10:
                my_money=current_money - int(current_money*0.1)
                rest = int(current_money*0.1)
            else:
                my_money = current_money
                rest = 0
                result[check_man]+=my_money
                break
            result[check_man]+=my_money
            if check_man =='-':
                break
            check_man=answer[check_man]
    return list(result.values())[1:]