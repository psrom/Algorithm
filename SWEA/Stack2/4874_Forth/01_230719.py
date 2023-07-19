T = int(input())

for tc in range(1, T + 1):
    calc = list(input().split())
    stack = []
    cnt = 0
    for token in calc:
        if token == ".":  # break point
            break

        if token.isdigit():  # 숫자인지 확인하고, 나중에 연산을 위해서 count
            cnt += 1
            stack.append(token)
        elif len(stack) >= 2: # pop 오류 방지
            x1 = int(stack.pop())
            x2 = int(stack.pop())

            if token == "+":
                stack.append(x2 + x1)  # stack에 저장되어 있기 때문에 먼저 나온 수가 뒤로 가도록
            elif token == "-":
                stack.append(x2 - x1)
            elif token == "*":
                stack.append(x2 * x1)
            elif token == "/":
                stack.append(x2 // x1)

    if cnt * 2 != len(calc):  # 피연산자와 연산자의 개수가 동일해야 함.
        print(f"#{tc} error")
    else:
        print(f"#{tc} {stack.pop()}")
