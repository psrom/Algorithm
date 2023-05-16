# 문제: https://www.acmicpc.net/problem/1157
s = input().upper()
unique = list(set(s)) # 중복 제거
cnt = [] # 알파벳 개수

for a in unique:
    c = s.count(a)
    cnt.append(c)

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    idx = cnt.index(max(cnt))
    print(unique[idx])
