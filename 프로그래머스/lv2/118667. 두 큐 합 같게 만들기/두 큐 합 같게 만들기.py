from collections import deque

def solution(queue1, queue2):
    answer = -2
    q1=deque(queue1)
    q2=deque(queue2)
    q1_sum=sum(queue1)
    q2_sum=sum(queue2)
    all_sum = q1_sum+q2_sum
    cnt=0
    limit=600000
    if all_sum%2==1:
        return -1
    else:
        while True:
            if q1_sum == q2_sum:
                break
            if cnt==limit:
                return -1
            if q1_sum > q2_sum:
                num = q1.popleft()
                q2.append(num)
                q1_sum-=num
                q2_sum+=num
                cnt+=1

            elif q1_sum < q2_sum:
                num = q2.popleft()
                q1.append(num)
                q1_sum+=num
                q2_sum-=num
                cnt+=1
    return cnt