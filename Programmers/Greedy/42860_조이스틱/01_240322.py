# https://school.programmers.co.kr/learn/courses/30/lessons/42860
def solution(name):
    l = len(name)
    move = l - 1
    answer = 0

    for i, char in enumerate(name):
        curr = ord(char)
        answer += min(curr - ord('A'), ord('Z') - curr + 1)

        # 연속된 A 문자열 찾기
        j = i + 1
        while j < l and name[j] == 'A':
            j += 1

        move = min([move, 2 * i + l - j, i + 2 * (l - j)])

    answer += move

    return answer
