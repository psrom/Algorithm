# https://www.acmicpc.net/problem/1107
def validation(channel, broken_buttons):
    for digit in str(channel):
        if digit in broken_buttons:
            return False
    return True


def min_button(N, M, broken_buttons):
    min_press = abs(N - 100)

    for channel in range(1000001):
        if validation(channel, broken_buttons):
            min_press = min(min_press, len(str(channel)) + abs(N - channel))

    return min_press


N = int(input())
M = int(input())
broken_buttons = set(input().split() if M > 0 else [])

result = min_button(N, M, broken_buttons)
print(result)
