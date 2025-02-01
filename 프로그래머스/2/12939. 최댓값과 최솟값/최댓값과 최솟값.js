function solution(s) {
    var answer = '';
    let s_arr = s.split(" ")
    let s_min = Infinity
    let s_max = -Infinity
    for (const num of s_arr) {
        s_min = Math.min(s_min,Number(num))
        s_max = Math.max(s_max,Number(num))
    }
    answer = String(s_min) + " " + String(s_max)
    return answer;
}