# 문제: 문자열에서 반복되는 문자를 지우고
# 지운 문자열에서 또 반복 문자 생성시 그 문자도 지우기
# 남은 문자 길이 출력, 남은 문자열이 없으면 0 출력
# EX) CAAABBA => 1

def find_duplication(q):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return 0 if not stack else len(stack)


T = int(input())
for tc in range(1, T + 1):
    s = input()
    print(f"#{tc} {find_duplication(s)}")
