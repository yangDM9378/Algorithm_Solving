def solution(cacheSize, cities):
    answer = 0
    cache_arr = []
    if cacheSize == 0:
        return len(cities)*5
    for city in cities:
        city = city.upper()
        if city in cache_arr:
            answer+=1
            cache_arr.remove(city)
            cache_arr.append(city)
        elif len(cache_arr) < cacheSize:
            answer+=5
            cache_arr.append(city)
        else:
            answer+=5
            cache_arr.pop(0)
            cache_arr.append(city)
    return answer