def solution(arr1, arr2):
    answer = []
    # 정답 배열 만들기
    for i in range(len(arr1)):
        answer.append([0]*len(arr2[0]))
    
    # 행 곱셈
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer