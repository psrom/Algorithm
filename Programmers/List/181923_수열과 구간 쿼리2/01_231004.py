# https://school.programmers.co.kr/learn/courses/30/lessons/181923
def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        sub_arr = arr[s: e + 1]
        
        temp = []
        for i in sub_arr:
            if i > k:
                temp.append(i)
                
        if len(temp) != 0:
            answer.append(min(temp))
        else:
            answer.append(-1)
        
    return answer