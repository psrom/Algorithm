# https://www.acmicpc.net/problem/1003
def fibo(n):
    if n == 0:
        return (1, 0)
    elif n == 1:
        return (0, 1)

    prev = (1, 0)  # 초기값 설정
    curr = (0, 1)

    for i in range(2, n + 1):
        next_term = (prev[0] + curr[0], prev[1] + curr[1])
        prev = curr
        curr = next_term

    return curr


for _ in range(int(input())):
    N = int(input())
    result = fibo(N)
    print(result[0], result[1])
