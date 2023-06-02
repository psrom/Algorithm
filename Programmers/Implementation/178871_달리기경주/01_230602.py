# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/178871
def solution(players, callings):
    answer = []
    hashmap = dict()
    
    for i,v in enumerate(players):
        hashmap[v] = i 
    
    print(hashmap)
    for call in callings:
        pre,post = hashmap[call]-1,hashmap[call]
        
        hashmap[players[pre]] = post
        hashmap[players[post]] = pre
        
        players[pre],players[post] = players[post],players[pre]
        
    return players