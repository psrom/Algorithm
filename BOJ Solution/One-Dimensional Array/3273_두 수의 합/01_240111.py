# https://www.acmicpc.net/problem/3273
import sys
input = sys.stdin.readline
N = int(input())
lst = list(map(int, input().rstrip().split()))
x = int(input())

check = [False] * 2000001
result = 0

for i in range(N):
    if x - lst[i] > 0 and check[x - lst[i]]:
        result += 1
    check[lst[i]] = True

print(result)