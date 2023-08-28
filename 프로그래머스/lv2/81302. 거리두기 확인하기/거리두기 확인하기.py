def check_di(y,x,place):
    distances=[(0,1),(1,0),(-1,0),(0,-1)]
    for distance in distances:
        for i in range(2):
            dy=y+distance[0]*(i+1)
            dx=x+distance[1]*(i+1)
            if dy<0 or dx<0 or dy>4 or dx>4: break
            if place[dy][dx]=='X':break
            if place[dy][dx]=='P':
                return False
    return True

def check_eo(y,x,place):
    distances=[(1,1),(1,-1),(-1,-1),(-1,1)]
    for distance in distances:
        dy=y+distance[0]
        dx=x+distance[1]
        if dy<0 or dx<0 or dy>4 or dx>4: continue
        if place[dy][dx]=='P':
            if place[y][dx]!='X'or place[dy][x]!='X':
                return False
    return True

def solution(places):
    answer = [1]*len(places)
    place_n = len(places)
    p = []
    for k in range(place_n):
        for y in range(5):
            for x in range(5):
                if places[k][y][x]=='P':
                    checked_di=check_di(y,x,places[k])
                    checked_eo=check_eo(y,x,places[k])
                    if checked_di+checked_eo != 2:
                        answer[k]=0
    return answer