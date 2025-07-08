function solution(n)
{
    var answer = 0;
    const str_n = String(n)
    for (v of str_n) {
        answer += Number(v)
    }
    return answer;
}