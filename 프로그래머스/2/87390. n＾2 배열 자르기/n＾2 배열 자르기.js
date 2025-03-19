function solution(n, left, right) {
    var answer = [];
    for (let i = left+1; i < right+2; i++) {
        if (i % n === 0) {
            answer.push(n)
        } else {
            if (i % n <= i / n) {
                answer.push(Math.floor(i / n) +1)
            } else {
                answer.push(i % n)
            }
        }
    }
    return answer;
}