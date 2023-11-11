T=int(input())
for _ in range(T):
    n=int(input())
    scores = list(map(int, input().split()))
    team_cnt = [0]*(max(scores)+1)
    for i in range(n):
        team_cnt[scores[i]]+=1
    record_team = []
    for i in range(len(team_cnt)):
        if team_cnt[i] == 6:
            record_team.append(i)

    record=[[0,[]] for _ in range((max(scores)+1))]
    score = 0
    for i in range(n):
        if scores[i] in record_team:
            score += 1
            if record[scores[i]][0] < 5:
                record[scores[i]][1].append(score)
                record[scores[i]][0]+=1
    result = 0
    min_score = 21e8
    for i in range(len(record)):
        if record[i][0]==0:
            continue
        ssum=sum(record[i][1][:4])
        if ssum<min_score:
            result = i
            min_score = ssum
        elif ssum==min_score:
            if record[i][1][-1] < record[result][1][-1]:
                result=i
                min_score=ssum
    print(result)