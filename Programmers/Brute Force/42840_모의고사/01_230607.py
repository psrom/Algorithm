def solution(answers):
    result = []

    s_1 = [1, 2, 3, 4, 5]
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]

    for i, answer in enumerate(answers):
        if s_1[i % 5] == answer:
            score[0] += 1
        if s_2[i % 8] == answer:
            score[1] += 1
        if s_3[i % 10] == answer:
            score[2] += 1
    
    m = max(score)
    for i in range(len(score)):
        if m == score[i]:
            result.append(i+1)

    return result