# https://school.programmers.co.kr/learn/courses/30/lessons/67256
def solution(numbers, hand):
    answer = ''
    keypads = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    L_location, R_location = (3, 0), (3, 2)  
    
    def get_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    for number in numbers:
        target_row, target_col = None, None
        for r in range(4):
            if number in keypads[r]:
                target_row = r
                target_col = keypads[r].index(number)
                break
                
        if number in [1, 4, 7]:
            answer += "L"
            L_location = (target_row, target_col)
        elif number in [3, 6, 9]:
            answer += "R"
            R_location = (target_row, target_col)
        else:
            L_distance = get_distance(target_row, target_col, L_location[0], L_location[1])
            R_distance = get_distance(target_row, target_col, R_location[0], R_location[1])
            
            if L_distance < R_distance:
                answer += "L"
                L_location = (target_row, target_col)
            elif L_distance > R_distance:
                answer += "R"
                R_location = (target_row, target_col)
            else:
                if hand == "left":
                    answer += "L"
                    L_location = (target_row, target_col)
                else:
                    answer += "R"
                    R_location = (target_row, target_col)

    return answer