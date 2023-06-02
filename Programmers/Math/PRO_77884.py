# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/77884
# 약수의 개수: 제곱수의 경우에만 홀수(이렇게도 풀이 가능)
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt = 0
        # 약수의 개수 세기
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        
        # 약수의 개수에 따라 연산        
        if cnt % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer