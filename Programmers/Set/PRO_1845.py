# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/1845
def solution(nums):
    get_mon = len(nums) // 2
    nums = set(nums)
    
    return min(get_mon , len(nums))