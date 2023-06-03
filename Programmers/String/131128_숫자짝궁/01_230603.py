# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/131128
# 다음에는 Counter 이용해서 풀어볼 것
def solution(X, Y):
    answer = ''
    X_dic = dict()
    Y_dic = dict()
    
    for x in X:
        if x not in X_dic:
            X_dic[x] = 1
        else:
            X_dic[x] += 1
    
    for y in Y:
        if y not in Y_dic:
            Y_dic[y] = 1
        else:
            Y_dic[y] += 1

# from collections import Counter
#     x = Counter(X)
#     y = Counter(Y)
# 이렇게 사용하면 위의 코드 전부 생략 가능
# 아래의 for문도 더 간단하게 돌릴 수 있음
    
    for x_key, x_val in enumerate(X_dic):
        for y_key, y_val in enumerate(Y_dic):
            if x_val == y_val:
                m = min(X_dic[x_val], Y_dic[y_val])
                answer += m * x_val
                
    if answer == '': return "-1"
    answer = sorted(answer, reverse=True)
    if answer[0] == "0": return "0"

    return "".join(answer)    
