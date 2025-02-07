function solution(s){
    var answer = true;
    
    const s_li = s.split('')
    const li = Array()
    
    while (s_li.length > 0) {
        const new_s1 = s_li.pop()
        if (li.length === 0) {
            li.push(new_s1)
        } else {
            const new_s2 = li.pop()
            if (new_s1 === "(" && new_s2 === ")") {
                continue
            } else {
                li.push(new_s2)
                li.push(new_s1)
            }
        }
    }
    if (li.length !== 0) {
        return false
    }
    return answer;
}