# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    stack = []
    answer = 0
    N = len(board)
    for move in moves:
        for i in range(N):
            doll = board[i][move - 1]
            if doll == 0:
                continue
            else:
                stack.append(doll)
                board[i][move - 1] = 0
                break
                
        if len(stack) > 1:
            if stack[-1] == stack[-2]:
                stack = stack[:-2]
                answer += 2
    
    return answer
