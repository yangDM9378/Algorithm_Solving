# man = []
# for _ in range(9):
#     man.append(int(input()))
# man_sort = sorted(man)
# result_man = list(set(man_sort))
# for i in range(0,7):
#     print(result_man[i])

def dfs(level, cnt):
    global result

    if len(result) == 7:
        if cnt == 100:
            print(result)
        return

    for i in range(level+1,9):
        result.append(dwarf[i])
        dfs(level+1, cnt+dwarf[i])
        print(level)
        result.pop()

dwarf = []
for _ in range(9):
    dwarf.append(int(input()))
result =[]
result_dwarf=[]
dfs(0,0)
