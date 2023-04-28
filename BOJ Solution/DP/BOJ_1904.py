n = int(input())

lst = [0] * 1000001 # n을 사용해서 list만들면 런타임 에러
lst[1] = 1
lst[2] = 2

# 조건 없이 for문 돌리면 메모리 초과
for i in range(3, n+1):
    lst[i] = (lst[i-1] + lst[i-2])%15746
print(lst[n])
