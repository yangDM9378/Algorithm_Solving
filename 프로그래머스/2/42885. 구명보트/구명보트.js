function solution(people, limit) {
    var answer = 0;
    let start = 0;
    let end = people.length - 1;
    people = people.sort((a, b) => b - a);
    while (start <= end) {
        let weight = people[start] + people[end];
        if (weight <= limit) {
            end -= 1;
        } 
        start += 1;
        answer += 1;
    }
    
    return answer;
}