def grouping(start, end):
    if start == end:
        return start

    mid = (start + end) // 2
    a = grouping(start, mid)
    b = grouping(mid + 1, end)
    return rsp(a, b)


def rsp(x, y):
    if cards[x] == cards[y]:
        return x
    elif cards[x] == 1:
        return x if cards[y] == 3 else y
    elif cards[x] == 2:
        return x if cards[y] == 1 else y
    else:
        return x if cards[y] == 2 else y


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    print(f"#{tc} {grouping(0, N-1) + 1}")
