def solution(m, musicinfos):
    answer = []
    m_music=[]
    for i in range(len(m)):
        if m[i] =='#':
            m_music[-1]+='#'
        else:
            m_music.append(m[i])
    
    for musicinfo in musicinfos:
        musicinfo = list(map(str, musicinfo.split(',')))
        start_HM= list(map(int, musicinfo[0].split(':')))
        end_HM = list(map(int, musicinfo[1].split(':')))
        time = 0
        time = (end_HM[0]-start_HM[0])*60+(end_HM[1]- start_HM[1])
        
        music=[]
        for i in range(len(musicinfo[3])):
            if musicinfo[3][i] =='#':
                music[-1]+='#'
            else:
                music.append(musicinfo[3][i])
                
        if time > len(music):
            music=music*(time//len(music))+music[:(time%len(music))]
        else:
            music = music[:time]
        print(music)
        for i in range(len(music)-len(m_music)+1):
            cnt=0  
            for j in range(len(m_music)):
                if m_music[j] == music[i+j]:
                    cnt+=1
                else:
                    cnt=0
                    break
            if cnt==len(m_music):
                answer.append([musicinfo[2], time])
                break
    if len(answer)==0:
        return "(None)"
    answer.sort(key=lambda x:-x[1])
    return answer[0][0]