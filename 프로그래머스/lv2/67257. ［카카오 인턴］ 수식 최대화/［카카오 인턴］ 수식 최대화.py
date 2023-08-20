from itertools import permutations
from collections import deque
def solution(expression):
    arr=[]
    max_result=0
    start=0
    for i in range(len(expression)):
        if expression[i] in ['-','+','*']:
            arr.append(expression[start:i])
            arr.append(expression[i])
            start=i+1
    arr.append(expression[start:])
    cal = ['-','+','*']
    cal_pers = list(permutations(cal))
    for cal_per in cal_pers:
        T_q = deque(arr)
        for per in cal_per:
            new_arr = []
            while True:
                if len(T_q)==0:
                    break
                new_q = T_q.popleft()
                if new_q == per:
                    first_num = new_arr.pop()
                    second_num = T_q.popleft()
                    if per=='-':
                        new_num = str(int(first_num)-int(second_num))
                        new_arr.append(new_num)
                    elif per=='+':
                        new_num = str(int(first_num)+int(second_num))
                        new_arr.append(new_num)
                    elif per=='*':
                        new_num = str(int(first_num)*int(second_num))
                        new_arr.append(new_num)
                else:
                    new_arr.append(new_q)
            T_q = deque(new_arr)
        result = abs(int(T_q.pop()))
        if max_result <result:
            max_result = result
    return max_result