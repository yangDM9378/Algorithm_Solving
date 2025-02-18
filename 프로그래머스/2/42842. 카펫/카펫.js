function solution(brown, yellow) {
    let answer = []
    let tp
    let rk
    for (let i = 1; i < Math.floor(yellow / 2) + 1; i++) {
        if (yellow % i === 0) {
            rk  = Math.floor(yellow / i)
            if ((i+rk) * 2 + 4 === brown) {
                tp = i
                break
            }
        }
    }
    if (yellow === 1) {
        return [3,3]
    }
    answer.push(rk + 2)
    answer.push(tp + 2)
    return answer;
}