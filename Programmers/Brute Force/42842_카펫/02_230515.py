def solution(brown, yellow):
    n = (brown - 4) // 2
    for i in range(n):
        x, y = i, n - i
        if x * y == yellow:
            return [y + 2, x + 2]
