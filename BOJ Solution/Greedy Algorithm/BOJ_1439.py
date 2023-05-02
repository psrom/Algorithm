# 문제: https://www.acmicpc.net/problem/1439
# 10, 01인 경우를 세야 함
s = list(input())
cnt = 0
for i in range(1, len(s)):
    if s[i-1] != s[i]: cnt += 1

if cnt % 2 == 0:
    print(cnt//2)
else:
    print((cnt-1)//2+1)