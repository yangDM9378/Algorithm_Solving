def solution(s):
    answer = True
    s_li = list(s)
    li = []
    while s_li:
        new_s1 = s_li.pop()
        if len(li) == 0:
            li.append(new_s1)
        else:
            new_s2 = li.pop()
            if new_s1 == "(" and new_s2 == ")":
                continue
            else:
                li.append(new_s2)
                li.append(new_s1)
    if len(li) != 0:
        return False
    return True