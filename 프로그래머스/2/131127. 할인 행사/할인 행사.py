def check_subp(dic):
    for val in dic.values():
        if val > 0:
            return False
    return True

def solution(want, number, discount):
    answer = 0
    cust_product = dict()
    for i in range(len(want)):
        cust_product[want[i]] = number[i]
    for i in range(0,10):
        if discount[i] in cust_product.keys():
            cust_product[discount[i]] -= 1
    answer += check_subp(cust_product)
    for i in range(0, len(discount)-10):
        if discount[i] in cust_product.keys():
            cust_product[discount[i]] += 1
        if discount[i+10] in cust_product.keys():
            cust_product[discount[i+10]] -= 1
        answer += check_subp(cust_product)
    return answer