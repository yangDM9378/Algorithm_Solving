from collections import Counter
def solution(weights):
    answer = 0
    weight_count = Counter(weights)
    for w in weight_count:
        answer += (weight_count[w] * (weight_count[w]-1)) / 2
        answer += weight_count[w] * weight_count[w*(4/3)]
        answer += weight_count[w] * weight_count[w*(4/2)]
        answer += weight_count[w] * weight_count[w*(3/2)]
    return answer