# https://www.acmicpc.net/problem/14889
from itertools import combinations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

min_diff = float('inf')

for team in combinations(range(N), N // 2):
    start_team = list(team)
    link_team = list(set(range(N)) - set(team))

    start_score, link_score = 0, 0

    for i in range(N // 2):
        for j in range(N // 2):
            start_score += S[start_team[i]][start_team[j]]
            link_score += S[link_team[i]][link_team[j]]

    diff = abs(start_score - link_score)
    min_diff = min(min_diff, diff)

print(min_diff)
