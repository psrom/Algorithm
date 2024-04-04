# https://www.acmicpc.net/problem/2504
brackets = input()
stack = []
temp = 1
ans = 0

for i in range(len(brackets)):
    b = brackets[i]
    if b == "(":
        temp *= 2
        stack.append(b)
    elif b == "[":
        temp *= 3
        stack.append(b)
    elif b == ")":
        if not stack or stack[-1] == "[":
            ans = 0
            break
        if brackets[i - 1] == "(":
            ans += temp
        temp //= 2
        stack.pop()
    else:
        if not stack or stack[-1] == "(":
            ans = 0
            break
        if brackets[i - 1] == "[":
            ans += temp
        temp //= 3
        stack.pop()

if stack:
    ans = 0

print(ans)
