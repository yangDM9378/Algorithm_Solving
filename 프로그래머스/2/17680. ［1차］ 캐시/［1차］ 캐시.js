function solution(cacheSize, cities) {
    var answer = 0;
    let cache_arr = []
    if (cacheSize === 0) {
        return cities.length * 5
    }
    for (let city of cities) {
        city = city.toUpperCase()
        if (cache_arr.includes(city)) {
            answer += 1
            cache_arr = cache_arr.filter((e) => e !== city)
            cache_arr.push(city)
        } else if (cache_arr.length < cacheSize) {
            answer += 5
            cache_arr.push(city)
        } else {
            answer += 5
            cache_arr.shift()
            cache_arr.push(city)
        }
    }
    return answer;
}