# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/160586#
def solution(keymap, targets):
    answer = []
    
    for target in targets:
        ans = 0
        for i in range(len(target)): # targets[0]의 "A"부터 순회
            cnt_lst = []
            for j in range(len(keymap)): # keymap[0]부터 순회
                if target[i] in keymap[j]:
                    cnt_lst.append(keymap[j].index(target[i]) + 1) # keymap[j]에서 idx찾고 + 1
            
            if len(cnt_lst) == 0: # keymap에 없는 경우 return -1
                ans = -1
                break
            elif len(cnt_lst) == 1: # cnt_lst의 원소가 1개인 경우 min 함수 적용 안 됨
                ans += cnt_lst[0]
            else:
                ans += min(cnt_lst)
                
        answer.append(ans)
    
    return answer
