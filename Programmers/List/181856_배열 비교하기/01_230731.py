# https://school.programmers.co.kr/learn/courses/30/lessons/181856
def solution(arr1, arr2):
    arr1_l, arr2_l = len(arr1), len(arr2)
    
    if arr1_l != arr2_l:
        return 1 if arr1_l > arr2_l else -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr2) > sum(arr1):
            return -1
        else:
            return 0
