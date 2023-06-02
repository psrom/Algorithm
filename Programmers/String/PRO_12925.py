def solution(s):
    answer = 0
    if s[0] == "-":
        num = int(s[1::])
        answer = -num

    elif s[0] == "+":
        answer = int(s[1::])

    else:
        answer = int(s)

    return answer

# =============================================
# int()는 -, + 부호를 인식해서 자동으로 정수 변환 해줌
def solution2(s):
    return int(s)
