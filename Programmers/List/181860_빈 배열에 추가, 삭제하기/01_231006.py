# https://school.programmers.co.kr/learn/courses/30/lessons/181860
def solution(arr, flag):
    X = []
    for i, condition in enumerate(flag):
        if condition:
            X.extend([arr[i]] * (arr[i] * 2))
        else:
            for _ in range(arr[i]):
                X.pop()
            
    return X