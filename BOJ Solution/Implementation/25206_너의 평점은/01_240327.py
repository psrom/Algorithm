# https://acmicpc.net/problem/25206
score_list = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5,
              "D0": 1.0, "F": 0.0}
lst = []
for _ in range(20):
    name, score, grade = input().split()
    if grade != "P":
        lst.append([float(score), grade])

answer = 0
total_score = 0
for i in range(len(lst)):
    total_score += lst[i][0]

total = 0
for score, grade in lst:
    total += score * score_list[grade]

print(total / total_score)
