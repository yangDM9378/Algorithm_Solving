function check_subp(dic) {
    for (let val of Object.values(dic)) {
        if (val > 0) {
            return false
        }
    }
    return true
}

function solution(want, number, discount) {
    var answer = 0;
    let cust_product = {}
    for (let i=0; i < want.length; i++) {
        cust_product[want[i]] = number[i]
    }
    for (let i = 0; i < 10; i++) {
        if ((discount[i] in cust_product)) {
            cust_product[discount[i]] -= 1
        }
    }
    answer += check_subp(cust_product)
    for (let i=0; i < discount.length-10; i++) {
        if (discount[i] in cust_product) {
            cust_product[discount[i]] += 1
        }
        if (discount[i+10] in cust_product) {
            cust_product[discount[i+10]] -= 1
        } 
        answer += check_subp(cust_product)
    }
    return answer;
}