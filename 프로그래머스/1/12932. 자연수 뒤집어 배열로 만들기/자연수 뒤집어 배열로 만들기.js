function solution(n) {
    var answer = [];
    let str_n = String(n)
    for (let i=str_n.length-1; i > -1;i--) {
        answer.push(Number(str_n[i]))
    }
    return answer;
}