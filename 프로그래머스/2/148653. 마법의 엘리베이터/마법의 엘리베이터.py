def solution(storey):
    result = 0
    while storey:
        stor = storey % 10
        if stor > 5:
            result += 10-stor
            storey += 10
        elif stor < 5:
            result += stor
        else:
            if (storey // 10) % 10 > 4:
                storey += 10
            result += stor        
        storey //= 10

    return result