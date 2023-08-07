from itertools import combinations
def solution(orders, course):
    result = []
    for i in course:
        course_orders = []
        order_dic={}
        for order in orders:
            order=sorted(order)
            combination=list(combinations(order,i))
            for com in combination:
                course_orders.append(com)
        for course_order in course_orders:
            order_dic[course_order] = order_dic.get(course_order,0)
            order_dic[course_order]+=1
        order_dic = order_dic.items()
        order_dic = sorted(order_dic, key=lambda x:-x[1])
        
        if len(order_dic)==0:continue
        max_order_cnt = order_dic[0][1]
        if max_order_cnt >= 2:
            for new_course in order_dic:
                if new_course[1]==max_order_cnt:
                    result.append(''.join(new_course[0]))
    result.sort()
    return result