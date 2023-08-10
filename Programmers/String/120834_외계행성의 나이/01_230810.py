# https://school.programmers.co.kr/learn/courses/30/lessons/120834
def solution(age):
    ages = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    age = str(age)
    
    answer = ""
    for n in age:
        answer += ages[int(n)]
        
    return answer