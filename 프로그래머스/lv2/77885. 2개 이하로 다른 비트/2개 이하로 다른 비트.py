def solution(numbers):
    result=[]
    for number in numbers:
        bin_number = bin(number)[2:]
        if number % 2 == 0:
            min_bin_number=bin_number[:-1]+'1'
            result.append(int(min_bin_number,2))
        else:  
            bin_number='0'+bin_number
            idx = bin_number.rfind('0')
            bin_number = list(bin_number)
            bin_number[idx]='1'
            bin_number[idx+1]='0'
            result.append(int(''.join(bin_number),2))
                
    return result
