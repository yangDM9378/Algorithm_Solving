function solution(elements) {
    var answer_set = new Set();
    for (let i=0; i < elements.length; i++) {
        let ssum = 0
        for (let j=0; j < elements.length; j++) {
            answer_set.add(ssum+=elements[j])
        }
        elements.push(elements.shift())
    }
    return answer_set.size;
}