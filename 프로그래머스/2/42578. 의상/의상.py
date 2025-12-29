def solution(clothes):
    hash_map = {}
    answer = 1
    
    for c in clothes:
        hash_map[c[1]] = hash_map.get(c[1], 1) + 1
        
    for value in hash_map.values():
        answer = answer * value
        
    return answer - 1