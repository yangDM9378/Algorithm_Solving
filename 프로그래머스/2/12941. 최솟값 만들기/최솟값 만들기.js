function solution(A,B){
    var answer = 0;
    A.sort((a,b) => a-b)
    B.sort((a,b) => b-a)
    for (i=0; i<=A.length-1; i++) {
        answer = answer + A[i]*B[i]
    }

    return answer;
}