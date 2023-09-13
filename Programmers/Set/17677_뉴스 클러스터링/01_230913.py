# https://school.programmers.co.kr/learn/courses/30/lessons/17677
def solution(str1, str2):
    # 1. 알파벳 2개로 slice
    str1, str2 = str1.lower(), str2.lower()
    lst_str1 = []
    for i in range(len(str1) - 1):
        check = str1[i:i+2]
        if check.isalpha():
            lst_str1.append(check)
    
    lst_str2 = []
    for i in range(len(str2) - 1):
        check = str2[i:i+2]
        if check.isalpha():
            lst_str2.append(check)
                   
                
    # 2. 다중집합 합집합
    temp = lst_str1.copy()
    union = lst_str1.copy()
    
    for s2 in lst_str2:
        if s2 not in temp:
            union.append(s2)
        else:
            temp.remove(s2)
    
    
    # 3. 다중집합 교집합
    intersection = []
    for s2 in lst_str2:
        if s2 in lst_str1:
            lst_str1.remove(s2)
            intersection.append(s2)
    
    
    # 4. 자카드 유사도
    if len(union) == 0:
        return 65536
    
    return int((len(intersection)/len(union)) * 65536)
