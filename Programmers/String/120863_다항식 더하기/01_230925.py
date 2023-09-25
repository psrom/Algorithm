# https://school.programmers.co.kr/learn/courses/30/lessons/120863
def solution(polynomial):
    terms = polynomial.split()

    x_coefficient, constant = 0, 0
    for term in terms:
        if 'x' in term:
            if term == 'x':
                x_coefficient += 1
            else:
                x_coefficient += int(term[:-1])

        elif term.isdigit():
            constant += int(term)

    if x_coefficient > 0:
        x_term = f"{x_coefficient}x" if x_coefficient != 1 else "x"
        if constant > 0:
            answer = f"{x_term} + {constant}"
        else:
            answer = x_term

    else:
        answer = str(constant)

    return answer