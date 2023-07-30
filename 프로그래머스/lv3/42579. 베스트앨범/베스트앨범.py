def solution(genres, plays):
    answer = []
    plays_dic={}
    genres_play_dic={}
    for i in range(len(genres)):
        plays_dic[genres[i]]=plays_dic.get(genres[i],0)+plays[i]
        genres_play_dic[genres[i]]=genres_play_dic.get(genres[i],[])
        genres_play_dic[genres[i]].append([i,plays[i]])
    
    plays_dic_sort = sorted(plays_dic.items(), key=lambda x:-x[1])
    for plays_sort_genres in plays_dic_sort:
        genres_play_sort = sorted(genres_play_dic[plays_sort_genres[0]], key = lambda x:(x[1],-x[0]))
        pre_cnt = len(answer)
        for i in range(len(genres_play_sort)):
            if pre_cnt+2 <= len(answer):
                break
            else:
                new_i = genres_play_sort.pop()[0]
                if new_i not in answer:
                    answer.append(new_i)
    return answer