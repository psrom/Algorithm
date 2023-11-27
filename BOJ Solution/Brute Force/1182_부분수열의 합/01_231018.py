# https://www.acmicpc.net/problem/1182
def solution(arr, S, current_sum, index):
    if current_sum == S:
        return 1

    if index == len(arr) or current_sum > S:
        return 0

    count_selected = solution(arr, S, current_sum + arr[index], index + 1)
    count_not_selected = solution(arr, S, current_sum, index + 1)

    return count_selected + count_not_selected


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

result = solution(numbers, S, 0, 0)
print(result)