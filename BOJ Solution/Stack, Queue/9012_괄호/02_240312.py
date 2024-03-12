# https://www.acmicpc.net/problem/9012
for _ in range(int(input())):
    s = input()
    stack = []

    check = True
    for a in s:
        if a == '(':
            stack.append(a)
        else:
            if not stack:
                check = False
                break
            else:
                stack.pop()

    if not stack and check:
        print('YES')
    else:
        print('NO')
