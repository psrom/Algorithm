# https://www.acmicpc.net/problem/11328
import sys
from collections import Counter

for _ in range(int(input())):
    first, second = sys.stdin.readline().rstrip().split()
    if Counter(first) == Counter(second):
        print("Possible")
    else:
        print("Impossible")
