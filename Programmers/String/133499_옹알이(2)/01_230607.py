# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/133499
# 문제 조건을 꼼꼼하게 읽을 것
def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    repeats = ["ayaaya", "yeye", "woowoo", "mama"]
    
    for x in babbling:
        for word in repeats:
            x = x.replace(word, "X") # 연속하는 발음 못함
        for word in words:
            x = x.replace(word, "O")
        
        isValid = True
        for char in x:
            if char != "O":
                isValid = False
                break
        if isValid == True:
            answer += 1
    
    return answer