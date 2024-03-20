# https://school.programmers.co.kr/learn/courses/30/lessons/250125
def solution(board, h, w):
    n = len(board)
    answer = 0

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = h + dx[i]
        ny = w + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if board[h][w] == board[nx][ny]:
                answer += 1

    return answer
