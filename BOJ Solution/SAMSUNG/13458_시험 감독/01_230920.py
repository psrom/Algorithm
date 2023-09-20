# https://www.acmicpc.net/problem/13458
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

answer = len(A)
A = [i - B for i in A]
for a in A:
    if a < 0:
        continue
    else:
        answer += a // C
        if a % C > 0:
            answer += 1

print(answer)
