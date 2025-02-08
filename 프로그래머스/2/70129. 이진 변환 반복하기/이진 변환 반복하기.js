function solution(s) {
    var answer = [0, 0];
    while (s !== '1') {
        answer[0] += 1
        const word = s.split('')
        const s_cnt1 = word.filter((el) => (el==='1')).length
        const s_cnt0 = word.filter((el) => (el==='0')).length
        answer[1] += s_cnt0
        s = s_cnt1.toString(2)
    }
    return answer;
}