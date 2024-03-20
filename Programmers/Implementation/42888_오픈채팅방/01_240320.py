# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    # 마지막 닉네임 찾기
    d = {}
    for user in record:
        user = user.split()
        if user[0] == "Enter":
            if user[1] not in d:
                d[user[1]] = user[2]
            else:
                d[user[1]] = user[2]

        elif user[0] == "Change":
            d[user[1]] = user[2]

    answer = []
    for user in record:
        user = user.split()
        name = d[user[1]]
        if user[0] == "Enter":
            answer.append(f"{name}님이 들어왔습니다.")
        elif user[0] == "Leave":
            answer.append(f"{name}님이 나갔습니다.")

    return answer
