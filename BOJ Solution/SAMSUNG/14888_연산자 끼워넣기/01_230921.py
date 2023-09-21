# https://www.acmicpc.net/problem/14888
N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

maxi, mini = float("-inf"), float("inf")


def dfs(depth, total, plus, minus, multiply, divide):
    global maxi, mini
    if depth == N:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return

    if plus:
        dfs(depth + 1, total + numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / numbers[depth]), plus, minus, multiply, divide - 1)


dfs(1, numbers[0], operators[0], operators[1], operators[2], operators[3])
print(maxi)
print(mini)
