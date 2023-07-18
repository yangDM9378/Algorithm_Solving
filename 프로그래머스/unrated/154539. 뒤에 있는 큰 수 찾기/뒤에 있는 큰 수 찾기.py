def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for idx in range(len(numbers)):
        number = numbers[idx]
        while stack and numbers[stack[-1]]< number:
            answer[stack.pop()] = number
        stack.append(idx)
    return answer