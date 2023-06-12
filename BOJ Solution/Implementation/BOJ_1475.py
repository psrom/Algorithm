# 문제: https://www.acmicpc.net/problem/1475
num = input()
plastic = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
dic = dict.fromkeys(plastic, 0)

lst = list(num)

for l in lst:
    if l == '9':
        dic['6'] += 1 # 6에 넣고 한번에 계산
    else:
        dic[l] += 1

share = dic["6"] // 2
dic["6"] -= share

m = max(dic.values())
print(m)