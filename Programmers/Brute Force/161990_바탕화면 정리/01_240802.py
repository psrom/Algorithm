# https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    start_x, start_y = float('inf'), float('inf')
    end_x, end_y = 0, 0
    
    for r in range(len(wallpaper)):
        for c in range(len(wallpaper[0])):
            if wallpaper[r][c] == "#":
                start_y = min(start_y, r)
                start_x = min(start_x, c)
                
                end_y = max(end_y, r)
                end_x = max(end_x, c)
                
    answer = [start_y, start_x, end_y + 1, end_x + 1]
    return answer
