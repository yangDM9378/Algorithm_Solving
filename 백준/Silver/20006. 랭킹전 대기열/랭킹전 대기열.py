rooms = []
level = []
p, m = map(int, input().split())
for _ in range(p):
    l,n = map(str, input().split())
    l=int(l)
    flag=False
    for i in range(len(rooms)):
        if level[i][0] <= l <= level[i][1] and len(rooms[i])<m:
            rooms[i].append((l,n))
            flag=True
            break
    if flag == False:
        rooms.append([])
        rooms[-1].append((l, n))
        level.append((l-10, l+10))
for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')
    room.sort(lambda x:x[1])
    for l,n in room:
        print(l,n)