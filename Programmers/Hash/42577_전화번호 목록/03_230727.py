# # https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    hash_map = {}

    for phone_number in phone_book:
        hash_map[phone_number] = 1

    for phone_number in phone_book:
        prefix = ""
        for digit in phone_number:
            prefix += digit
            if prefix in hash_map and prefix != phone_number:
                return False
    return True