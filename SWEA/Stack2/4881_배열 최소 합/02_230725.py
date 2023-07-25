# 백트래킹 + 가지치기
def get_min_sum(row, visited, current_sum):
    global min_sum

    # 탈출 조건: 행이 N과 같을 때는 구할 수 있는 모든 합을 구한 상태
    if row == N:
        min_sum = min(min_sum, current_sum)
        return min_sum

    # 가지치기 코드 없으면 제한시간 초과 됨
    if current_sum >= min_sum:
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = True
            # 가능한 조합 탐색
            get_min_sum(row + 1, visited, current_sum + board[row][col])
            visited[col] = False  # 답을 찾지 못한 경우 False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')
    visited = [False] * N
    get_min_sum(0, visited, 0)
    print(f"#{tc} {min_sum}")