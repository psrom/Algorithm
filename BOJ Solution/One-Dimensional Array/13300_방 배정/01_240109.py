# https://www.acmicpc.net/problem/13300
import sys
N, K = map(int, input().split())
students = [[0, 0] for _ in range(6)]
for _ in range(N):
    S, Y = map(int, sys.stdin.readline().split())
    students[Y - 1][S] += 1

answer = 0
for student in students:
    for s in student:
        answer += s // K
        if s % K != 0:
            answer += 1

print(answer)
