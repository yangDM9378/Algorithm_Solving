function solution(x, n) {
    let answer  = Array(n).fill().map((v,i) => x*(i+1))
    return answer;
}