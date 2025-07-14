def solution(topping):
    answer = 0
    topping_l = [0]*(max(topping)+1)
    topping_r = [0]*(max(topping)+1)
    l_count = 0
    r_count = 0
    for topp in topping:
        topping_r[topp] += 1
        if topping_r[topp] == 1:
            r_count+=1
    for topp in topping:
        topping_r[topp] -= 1
        topping_l[topp] += 1
        if topping_r[topp] == 0:
            r_count-=1
        if topping_l[topp] == 1:
            l_count+=1
        if r_count == l_count:
            answer+=1
    return answer