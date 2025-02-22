function solution(people, limit) {
    var answer = 0;
    let start = 0;
    let end = people.length - 1;
    
    // 오름차순으로 정렬
    people.sort((a, b) => a - b);
    
    while (start <= end) {
        let weight = people[start] + people[end];
        if (weight <= limit) {
            // 두 사람이 함께 탈 수 있으면 둘 다 태운다
            start += 1;
        }
        // 가장 무거운 사람은 항상 태운다
        end -= 1;
        answer += 1;  // 구명보트 한 번 사용
    }
    
    return answer;
}