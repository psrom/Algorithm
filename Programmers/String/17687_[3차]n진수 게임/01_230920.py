# https://school.programmers.co.kr/learn/courses/30/lessons/17687
def solution(n, t, m, p):
    def convert_to_base(num, base):
        if num == 0:
            return '0'
        digits = []
        while num > 0:
            num, mod = divmod(num, base)
            if mod >= 10:
                digits.append(chr(ord('A') + mod - 10))
            else:
                digits.append(str(mod))
        return ''.join(digits[::-1])

    num_list = []
    i = 0
    while len(num_list) < t * m:
        num_list.extend(list(convert_to_base(i, n)))
        i += 1

    answer = ''.join(num_list[p - 1::m])[:t]

    return answer
