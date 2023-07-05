def solution(s):
    stack = []
    for item in s:
        if len(stack) == 0:
            stack.append(item)
        else:
            pre_item= stack.pop()
            if pre_item!=item:
                stack.append(pre_item)
                stack.append(item)
    if len(stack)==0:
        answer=1
    else:
        answer=0
    return answer