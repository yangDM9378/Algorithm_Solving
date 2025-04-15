function solution(s) {
    let arr = []
    s = s.slice(1,-1)
    let li = ''
    for (let i of s) {
        if (i === '{') {
            li = '';
        } else if (i === '}'){
            arr.push(li.split(','))
            li = '';
        } else {
            li += i
        }
    }
    
    arr.sort((a,b) => a.length - b.length);
    const answer =[]
    const set_arr = new Set();
    for (let li of arr) {
        for (let num of li) {
            num = parseInt(num)
            if (!set_arr.has(num)) {
                answer.push(num);
                set_arr.add(num)
            }
        }
    }
    return answer;
}