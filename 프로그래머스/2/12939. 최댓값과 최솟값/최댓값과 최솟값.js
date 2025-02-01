function solution(s) {
    const s_arr = s.split(" ")
    const answer = Math.min(...s_arr) + " " + Math.max(...s_arr)
    return answer;
}