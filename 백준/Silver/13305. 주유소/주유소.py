n=int(input())
directs = list(map(int, input().split()))
costs = list(map(int, input().split()))
total_cost = 0
current_cost = costs[0]
current_direct = directs[0]
for i in range(1,n-1):
    if current_cost > costs[i]:
        total_cost += current_cost*current_direct
        current_cost = costs[i]
        current_direct = directs[i]
    else:
        current_direct += directs[i]
total_cost += current_cost*current_direct
print(total_cost)
