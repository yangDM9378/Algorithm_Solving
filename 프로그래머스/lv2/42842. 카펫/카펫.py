def solution(brown, yellow):
    S=brown+yellow
    wh=[]
    for w in range(1,S+1):
        for h in range(1,S+1):
            if w<h:
                break
            if w*h == S:
                y=(w-2)*(h-2)
                b=S-y
                if brown==b and yellow==y:
                    return [w,h]