from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    steps = [[-1] * m for _ in range(n)]
    steps[0][0] = 1
    
    que = deque([(0, 0)])
    
    while que:
        x, y = que.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and steps[nx][ny] == -1:
                steps[nx][ny] = steps[x][y] + 1
                que.append((nx, ny))
                
    return steps[n-1][m-1]