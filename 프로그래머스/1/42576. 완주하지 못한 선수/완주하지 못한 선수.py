def solution(participant, completion):
    hash_map = {}
    
    for p in participant:
        hash_map[p] = hash_map.get(p, 0) + 1
        
    for c in completion:
        hash_map[c] -= 1
        
    for p in hash_map:
        if hash_map[p] > 0:
            return p
            
