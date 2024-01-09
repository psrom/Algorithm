# https://www.acmicpc.net/problem/10808
s = input()
alphabets = [0 for _ in range(26)]
for i in s:
    alphabets[ord(i)-97] += 1

print(*alphabets)
