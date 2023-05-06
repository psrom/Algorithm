# 문제: https://www.acmicpc.net/problem/1049
n, m = map(int, input().split())
set_ls, single_ls =[], []
for _ in range(m):
    s, t = (map(int, input().split()))
    set_ls.append(s)
    single_ls.append(t)

s = n//6 # 세트(6개) 수
t = n % 6 # 낱개

price = []
for i in range(m):
    if single_ls[i] * 6 < set_ls[i]:
        set_ls[i] = single_ls[i] * 6 # 작은 수로 업데이트

min_set, min_single = min(set_ls), min(single_ls)

# 1) 세트 + 개당 가격
price.append(min_set*s + min_single*t)
# 2) 세트로 다 사는 경우 가격
if t != 0: price.append(min_set * (s + 1))

print(min(price))
