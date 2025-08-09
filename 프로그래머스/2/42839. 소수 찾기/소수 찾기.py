from itertools import permutations
import math

def solution(numbers):
    results = set()
    for i in range(1, len(numbers)+1):
        for per_num in permutations(numbers,i):
            results.add(int("".join(per_num)))
    max_n = max(results)
    
    prime_check = [True] * (max_n+1)
    prime_check[0], prime_check[1] = False, False
    for i in range(2, int(math.sqrt(max_n))):
        if prime_check[i]:
            for k in range(i*i, max_n + 1, i):
                prime_check[k] = False
    
    answer=0
    for result in results:
        if prime_check[result]:
            answer+=1
    return answer