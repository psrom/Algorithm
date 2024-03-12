# https://www.acmicpc.net/problem/3986
ans = 0
for _ in range(int(input())):
    s = input()
    stack = []

    for a in s:
        if not stack:
            stack.append(a)

        else:
            if stack[-1] == a:
                stack.pop()
            else:
                stack.append(a)

    if not stack:
        ans += 1

print(ans)