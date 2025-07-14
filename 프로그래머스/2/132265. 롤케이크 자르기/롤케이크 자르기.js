function solution(topping) {
    let answer = 0;
    let r = Array(10001).fill(0) 
    let l = Array(10001).fill(0)
    let r_c = 0
    let l_c = 0
    for (let i = 0; i < topping.length; i++) {
        r[topping[i]] += 1
        if (r[topping[i]] === 1) {
           r_c += 1 
        }
    }
    for (let i = 0; i < topping.length; i++) {
        r[topping[i]] -= 1
        l[topping[i]] += 1
        if (r[topping[i]] === 0) {
            r_c -= 1
        }
        if (l[topping[i]] === 1) {
            l_c += 1
        }
        if (l_c === r_c) {
            answer += 1
        } else if (l_c > r_c) {
            return answer
        }
    }
    return answer;
}