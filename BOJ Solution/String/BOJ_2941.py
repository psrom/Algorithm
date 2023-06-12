# 문제: https://www.acmicpc.net/problem/2941
s = input()
cro = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

# dz= 먼저 처리
for i in range(len(s)-2):
    if s[i:i+3] == 'dz=':
        s = s[:i] + "#" + s[i+3:]

# 나머지 문자 처리
for i in range(len(s)-1):
    if s[i:i+2] in cro:
        s = s[:i] + "#" + s[i+2:]

print(len(s))
