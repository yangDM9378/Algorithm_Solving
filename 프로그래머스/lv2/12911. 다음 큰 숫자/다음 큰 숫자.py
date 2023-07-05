def solution(n):
    bin_n = bin(n)[2:]
    bin_n_1 = bin_n.count('1')
    for i in range(n+1, 1000001):
        bin_next_n = bin(i)[2:]
        if bin_next_n.count('1') == bin_n_1:
            result=i
            break
    return result