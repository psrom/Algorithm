# https://www.acmicpc.net/problem/1919
from collections import Counter

first = input()
second = input()

first_counter = Counter(first)
second_counter = Counter(second)

diff = sum(abs(first_counter[char] - second_counter[char]) for char in (first_counter | second_counter))
print(diff)
