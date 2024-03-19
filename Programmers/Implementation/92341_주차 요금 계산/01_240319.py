import math


def cal_time(in_time, out_time):
    in_hour, in_minute = map(int, in_time.split(":"))
    out_hour, out_minute = map(int, out_time.split(":"))

    if in_minute > out_minute:
        out_hour -= 1
        out_minute += 60

    total_hour = out_hour - in_hour
    total_minute = out_minute - in_minute

    return total_hour * 60 + total_minute


def solution(fees, records):
    base_time, base_rate, unit_time, unit_rate = fees

    d = {}
    for record in records:
        time, number, statement = record.split()
        if number in d.keys():
            d[number].append(time)
        else:
            d[number] = [time]

    result = {}
    for key, val in d.items():
        total = 0
        for i in range(0, len(val) - 1, 2):
            total += cal_time(val[i], val[i + 1])

        if len(val) % 2 != 0:
            total += cal_time(val[-1], "23:59")

        result[key] = total
    result = sorted(result.items(), key=lambda x: x[0])

    answer = []
    for k, val in result:
        if val < base_time:
            answer.append(base_rate)
        else:
            cost = math.ceil((val - base_time) / unit_time) * unit_rate
            answer.append(base_rate + cost)

    return answer
