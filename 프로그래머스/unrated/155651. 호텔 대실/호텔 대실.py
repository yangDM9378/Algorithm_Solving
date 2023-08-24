def solution(book_time):
    time = []
    for book in book_time:
        sh,sm = map(int, book[0].split(':'))
        eh,em = map(int, book[1].split(':'))
        start=sh*60+sm
        end = eh*60+em+10
        time.append([start,end])
    time.sort(key=lambda x:x[0])
    leave = []
    for new_time in time:
        if not leave:
            leave.append(new_time)
        else:
            if leave[-1][1] > new_time[0]:
                leave.append(new_time)
            else:
                leave.pop()
                leave.append(new_time)
        
        leave.sort(key=lambda x:-x[1])
    return len(leave)