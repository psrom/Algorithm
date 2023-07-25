# permutations는 N이 10 이상일 때는 사용 X
# 런타임 에러 발생 => 백트래킹으로 풀 것
from itertools import permutations

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = [i for i in range(N)]
    board = [list(map(int, input().split())) for _ in range(N)]

    col_idx = list(permutations(lst, N))  # column의 인덱스 미리 구하기

    min_sum = float('inf')  # 최소합 무한으로 초기화
    for c in col_idx:
        s = 0
        for r in range(N):
            s += board[r][c[r]]
        min_sum = min(min_sum, s)
    print(f"#{tc} {min_sum}")
