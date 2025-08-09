from itertools import permutations
import math

def primenumber(x):
    if x in [0,1]:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    results = set()
    for i in range(1, len(numbers)+1):
        per_number = permutations(numbers, i)
        for per_num in per_number:
            num = int("".join(per_num))
            results.add(int(num))
    answer = 0
    for result in results:
        if primenumber(result):
            answer += 1
    return answer