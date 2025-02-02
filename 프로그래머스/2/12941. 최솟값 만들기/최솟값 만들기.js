function solution(A,B){
    var answer = 0;
    A.sort((a,b) => a-b)
    B.sort((a,b) => b-a)
    return A.reduce((total, A_num, idx) => {return total+A_num*B[idx]},0)
}