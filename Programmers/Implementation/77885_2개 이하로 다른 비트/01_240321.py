def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            temp = '0' + bin(num)[2:]
            temp_lst = list(temp)
            r_idx = temp.rfind('0')

            temp_lst[r_idx] = '1'
            temp_lst[r_idx + 1] = '0'

            temp_str = "".join(temp_lst)

            answer.append(int(temp_str, 2))

    return answer
