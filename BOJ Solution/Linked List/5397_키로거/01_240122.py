# https://www.acmicpc.net/problem/5397
# 19:12-19:51
for _ in range(int(input())):
    l = []
    r = []
    s = input()

    for c in s:
        if c == '<':
            if l:
                r.append(l.pop())
        elif c == '>':
            if r:
                l.append(r.pop())
        elif c == '-':
            if l:
                l.pop()
        else:
            l.append(c)

    l.extend(reversed(r))
    print(''.join(l))
