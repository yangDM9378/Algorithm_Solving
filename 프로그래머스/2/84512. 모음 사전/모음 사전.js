   
function solution(word) {
    const word_alpha = ['A','E','I','O','U']

    let answer = 0;
    let checked = false;
    
    function dfs(currentWord) {
        if (currentWord === word) {
            checked = true;
            return;
        }
        if (currentWord.length >= 5 || checked) return;
        for (let alpha of word_alpha){
            if (checked) return;
            answer ++
            dfs(currentWord+alpha)
        }
    }
    dfs('')
    return answer;
}