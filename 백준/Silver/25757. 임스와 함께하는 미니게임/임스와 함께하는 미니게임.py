n,game = map(str, input().split())

game_list = {'Y':2,'F':3,'O':4}
game_cnt = game_list[game]

set_members = set()
for _ in range(int(n)):
    set_members.add(input())

arr_member = list(set_members)
print(len(arr_member)//(game_cnt-1))