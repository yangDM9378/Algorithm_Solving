def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        cnt=0
        result = 0
        for sk in skill_tree:
            if sk in skill:
                print(skill[cnt], sk)
                if skill[cnt]!=sk:
                    result = -1
                    break
                cnt+=1
        print(result)
        if result==0:
            answer+=1
    return answer