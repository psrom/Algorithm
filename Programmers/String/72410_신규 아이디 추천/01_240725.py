# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1단계: 소문자 변환
    id_1 = new_id.lower()

    # 2단계: 소문자, 숫자, -, _, .가 아닌 문자 제거
    id_2 = ''

    for t in id_1:
        if t.isalpha() or t.isdigit() or t in '-_.':
            id_2 += t

    # 3단계: 마침표가 2번 이상 연속되면 하나의 마침표로 치환
    while '..' in id_2:
        id_2 = id_2.replace('..', '.')
    id_3 = id_2

    # 4단계: .가 처음이나 끝에 위치하면 제거
    id_4 = id_3.strip('.')

    # 5단계: 빈 문자열이면 new_id에 a 대입
    if id_4 == "":
        id_5 = 'a'
    else:
        id_5 = id_4

    # 6단계: 길이 15자 제한, 제거 후 마침표가 끝에 위치하면 제거
    id_6 = id_5[:15].rstrip('.')

    # 7단계: 2자 이하면 마지막 문자를 길이가 3이 될때까지 반복
    while len(id_6) < 3:
        id_6 += id_5[-1]

    answer = id_6
    return answer
