# 문제: https://www.acmicpc.net/problem/11723
# 입력이 너무 커서 sys안 하고 사용하면 시간 초과
# discard()을 사용하면 값이 없어도 오류 X 값이 있는 경우에는 remove
# =========================================================
import sys
s = set()
for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        if order[0] == "all":
            s = set(i for i in range(1, 21))
        else:
            s = set()

    else:
        f, x = order[0], order[1]
        x = int(x)

        if f == "add":
            s.add(x)
        elif f == "remove":
            s.discard(x)
        elif f == "check":
            if x in s:
                print(1)
            else:
                print(0)
        elif f == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)
