# https://www.acmicpc.net/problem/11328
import sys
from collections import Counter

for _ in range(int(input())):
    first, second = sys.stdin.readline().rstrip().split()
    f = Counter(first)
    check = True
    for letter in second:
        if letter in f:
            f[letter] -= 1
        else:
            check = False

    for val in f.values():
        if val != 0:
            check = False

    print("Possible" if check else "Impossible")
