# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/17680
# LRU: 오래된 캐시부터 지우기
def solution(cacheSize, cities):
    cities = [i.lower() for i in cities]  # 소문자로 변환

    cache = []  # 캐시 배열
    time = 0  # 소요 시간

    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            time += 1
        else:
            if len(cache) < cacheSize:
                cache.append(city)
                time += 5
            else:
                cache.append(city)
                cache.pop(0)
                time += 5

    return time