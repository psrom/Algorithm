# 문제: https://www.acmicpc.net/problem/2891
n, s, r = map(int, input().split())
broken = list(map(int, input().split()))
one_more = list(map(int, input().split()))

team = [1] * n

for i in range(s):
    team[broken[i]-1] -= 1

for j in range(r):
    team[one_more[j]-1] += 1

for k in range(n):
    if team[k] == 0:
        if k > 0 and team[k-1] == 2:
            team[k-1] = 1
            team[k] = 1
        elif k < n-1 and team[k+1] == 2:
            team[k] = 1
            team[k+1] = 1

answer = team.count(0)
print(answer)