# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/76502

def bracket(s):
    stack = []
    for i in s:
        if len(stack) == 0:
            stack.append(i)
        else:
            if i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(i)
    return 1 if len(stack) == 0 else 0


def solution(s):
    ans = 0
    for i in range(len(s)):
        if bracket(s):  ans += 1
        s = s[1:] + s[:1]
    return ans
